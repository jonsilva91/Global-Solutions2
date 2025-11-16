"""
Treino de um modelo simples de risco de estresse com dados simulados.
"""

from pathlib import Path
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

BASE_DIR = Path(__file__).resolve().parents[2]
MODELS_DIR = BASE_DIR / "models"
MODELS_DIR.mkdir(exist_ok=True)

def generate_dummy_data(n=200):
    # q1 motivação (1-5), q2 cansaço (1-5), q3 stress (1-5)
    rng = np.random.default_rng(42)
    q1 = rng.integers(1, 6, n)
    q2 = rng.integers(1, 6, n)
    q3 = rng.integers(1, 6, n)
    # risco alto se stress e cansaço altos e motivação baixa
    y = ((q3 >= 4) & (q2 >= 4) & (q1 <= 3)).astype(int)
    X = np.vstack([q1, q2, q3]).T
    return X, y


def train_and_save():
    X, y = generate_dummy_data()
    model = LogisticRegression()
    model.fit(X, y)
    out_path = MODELS_DIR / "stress_model.pkl"
    joblib.dump(model, out_path)
    print(f"Modelo de estresse salvo em {out_path}")


if __name__ == "__main__":
    train_and_save()
