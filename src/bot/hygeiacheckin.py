"""
Hygeia – agente de bem-estar.
"""

import re
import sys
from pathlib import Path

import numpy as np
import joblib

from .intents_classifier import classify_intent

# ========= AJUSTE DE PATH (como você já estava fazendo) =========
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

# ========= CARREGAMENTO DO MODELO DE ESTRESSE =========
# Usamos o arquivo gerado pelo seu script de treino (models/stress_model.pkl)
BASE_DIR = ROOT
MODEL_PATH = BASE_DIR / "models" / "stress_model.pkl"

_stress_model = None  # cache em memória


def _get_stress_model():
    """
    Carrega o modelo de estresse a partir do arquivo .pkl.
    Não muda o seu stress_model.py, só reutiliza o output dele.
    """
    global _stress_model
    if _stress_model is None:
        if not MODEL_PATH.exists():
            # Se o modelo ainda não foi treinado/salvo, avisa de forma amigável.
            raise FileNotFoundError(
                f"Arquivo de modelo não encontrado em {MODEL_PATH}. "
                "Certifique-se de rodar o script de treino do stress_model antes."
            )
        _stress_model = joblib.load(MODEL_PATH)
    return _stress_model


def predict_stress_risk(q1: int, q2: int, q3: int):
    """
    Usa o modelo de estresse salvo para prever risco.

    Retorna:
        label (int): 0 = risco não alto, 1 = risco alto
        prob (float): probabilidade do risco ser alto (0.0–1.0)
    """
    model = _get_stress_model()
    X = np.array([[q1, q2, q3]])
    prob = model.predict_proba(X)[0, 1]
    label = int(model.predict(X)[0])
    return label, float(prob)


# ========= LÓGICA DA HYGEIA =========

CHECKIN_PROMPT = (
    "🧠 Vamos fazer um check-in rápido de bem-estar.\n\n"
    "Responda com **três números de 1 a 5**, separados por espaço ou vírgula, assim: `3 4 5`.\n\n"
    "1) Numa escala de 1 a 5, quão **motivado(a)** você se sente hoje?\n"
    "2) De 1 a 5, quão **cansado(a)** você está?\n"
    "3) De 1 a 5, quão **estressado(a)** você se sente?\n"
)


def _parse_scores(text: str):
    """
    Extrai três números entre 1 e 5 da mensagem do usuário.
    Ex.: '3 4 5' ou 'Motivado 4, cansado 2, stress 5' -> [4, 2, 5]
    """
    nums = re.findall(r"[1-5]", text)
    if len(nums) >= 3:
        return list(map(int, nums[:3]))
    return None


def handle_message(user_id: str, text: str) -> str:
    intent = classify_intent(text)

    # 1) Fluxo principal: usuário pediu um checkin
    if intent == "checkin":
        return CHECKIN_PROMPT

    # 2) Tentativa de interpretar resposta com 3 notas
    scores = _parse_scores(text)
    if scores:
        q1, q2, q3 = scores

        # Cabeçalho comum (sempre mostrar o que ele respondeu)
        header = (
            f"Obrigado por compartilhar seu estado hoje 🙏\n\n"
            f"**Motivação:** {q1}\n"
            f"**Cansaço:** {q2}\n"
            f"**Stress:** {q3}\n\n"
        )

        try:
            label, prob = predict_stress_risk(q1, q2, q3)
            prob_pct = round(prob * 100)
        except Exception:
            # Se der qualquer erro ao carregar/usar o modelo, não quebrar o fluxo
            return (
                header
                + "Tentei avaliar o risco de estresse com o modelo interno, "
                "mas tive um problema ao acessar o modelo de ML.\n\n"
                "Mesmo assim, é importante você cuidar de descanso, sono e limites. "
                "Se sentir que está sobrecarregado(a), vale conversar com alguém de confiança "
                "ou buscar apoio profissional. 💚"
            )

        if label == 1:
            # risco alto
            return (
                header
                + f"O modelo sinalizou **risco elevado de estresse** (aprox. {prob_pct}% de probabilidade).\n\n"
                "✨ Algumas sugestões:\n"
                "- Veja se consegue fazer pequenas pausas ao longo do dia;\n"
                "- Se possível, converse com alguém de confiança sobre como você está se sentindo;\n"
                "- Considere buscar apoio de um(a) profissional de saúde mental.\n\n"
                "⚠️ Se em algum momento você tiver pensamentos de se machucar ou de não querer mais viver,\n"
                "procure ajuda imediatamente. No Brasil, você pode ligar **188** (CVV) ou buscar um serviço\n"
                "de emergência na sua região.\n\n"
                "Posso te ajudar a acompanhar isso com novos check-ins ao longo da semana. 💛"
            )
        else:
            # risco não-alto
            return (
                header
                + f"O modelo **não indicou risco alto de estresse** (aprox. {prob_pct}%).\n\n"
                "Mesmo assim, é sempre importante cuidar de sono, descanso e limites.\n"
                "Se quiser, posso te ajudar com mais check-ins ou com organização de tarefas "
                "pra evitar sobrecarga. 🙂"
            )

    # 3) fallback: mensagem genérica da Hygeia
    return (
        "Sou a **Hygeia**, agente focada em bem-estar. 💚\n\n"
        "- Se você quiser fazer um check-in, basta digitar **`checkin`**.\n"
        "- Ou me mande três notas (1–5) de motivação, cansaço e stress, como `3 4 5`."
    )
