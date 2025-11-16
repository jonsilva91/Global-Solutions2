from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import logging
import joblib
import os
import sqlite3
from pathlib import Path

# Configuração básica de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("human_ops_api")

BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "config" / "db" / "human_ops.db"
MODELS_DIR = BASE_DIR / "models"

app = FastAPI(
    title="HUM.A.N OPS API",
    description="API para bem-estar, produtividade, sustentabilidade e inclusão.",
    version="0.1.0",
)

# ==== MODELOS Pydantic ====


class CheckinRequest(BaseModel):
    colaborador_id: int
    q1_motivacao: int  # 1-5
    q2_cansaco: int    # 1-5
    q3_stress: int     # 1-5
    comentario: Optional[str] = None


class StressScoreResponse(BaseModel):
    risk_score: float
    risk_level: str


class EnergyStatusResponse(BaseModel):
    current_kwh: float
    daily_total: float
    anomaly_flag: bool


# ==== HELPERS de BD ====


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


# ==== Carregar modelos (se existirem) ====


def load_model(path: Path):
    if path.exists():
        return joblib.load(path)
    logger.warning("Modelo não encontrado em %s, usando fallback.", path)
    return None


STRESS_MODEL = load_model(MODELS_DIR / "stress_model.pkl")
ENERGY_MODEL = load_model(MODELS_DIR / "energy_anomaly.pkl")


# ==== ROTAS ====


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "HUM.A.N OPS API rodando."}


@app.post("/checkin", response_model=StressScoreResponse)
def criar_checkin(payload: CheckinRequest):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO checkin (id_colab, dt, q1, q2, q3, texto_opcional)
        VALUES (?, datetime('now'), ?, ?, ?, ?)
        """,
        (
            payload.colaborador_id,
            payload.q1_motivacao,
            payload.q2_cansaco,
            payload.q3_stress,
            payload.comentario,
        ),
    )
    conn.commit()
    conn.close()

    # Feature simples: inversão de escala pra ilustrar
    features = [
        payload.q1_motivacao,
        payload.q2_cansaco,
        payload.q3_stress,
    ]

    if STRESS_MODEL is not None:
        import numpy as np

        proba = STRESS_MODEL.predict_proba([features])[0][1]
    else:
        # fallback simples: média normalizada
        proba = (payload.q3_stress + payload.q2_cansaco) / 10.0

    if proba < 0.33:
        level = "baixo"
    elif proba < 0.66:
        level = "moderado"
    else:
        level = "alto"

    logger.info(
        "Check-in registrado para colaborador %s, risco %.2f (%s)",
        payload.colaborador_id,
        proba,
        level,
    )

    return StressScoreResponse(risk_score=round(proba, 3), risk_level=level)


@app.get("/energia/status", response_model=EnergyStatusResponse)
def energia_status():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        """
        SELECT kwh, dt
        FROM energia
        ORDER BY dt DESC
        LIMIT 1
        """
    )
    row = cur.fetchone()

    if not row:
        return EnergyStatusResponse(
            current_kwh=0.0, daily_total=0.0, anomaly_flag=False
        )

    current_kwh = float(row["kwh"])

    cur.execute(
        """
        SELECT SUM(kwh) as total
        FROM energia
        WHERE date(dt) = date('now')
        """
    )
    total_row = cur.fetchone()
    daily_total = float(total_row["total"] or 0.0)

    # Usa modelo se existir, senão regra simples
    anomaly_flag = False
    if ENERGY_MODEL is not None:
        import numpy as np

        pred = ENERGY_MODEL.predict([[current_kwh]])
        anomaly_flag = bool(pred[0] == -1)
    else:
        anomaly_flag = current_kwh > 2.0  # exemplo hardcoded

    conn.close()
    return EnergyStatusResponse(
        current_kwh=current_kwh,
        daily_total=daily_total,
        anomaly_flag=anomaly_flag,
    )
