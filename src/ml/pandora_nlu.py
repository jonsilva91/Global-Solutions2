import json
import random
import numpy as np

from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "intents.json"
MODEL_PATH = BASE_DIR / "models" / "pandora_intent.pkl"
VECTORIZER_PATH = BASE_DIR / "models" / "pandora_vectorizer.pkl"


def load_intents():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data["intents"]


def train_pandora_model():
    intents = load_intents()

    X_text = []
    y = []
    tags = []

    for intent in intents:
        tag = intent["tag"]
        for pattern in intent["patterns"]:
            X_text.append(pattern)
            y.append(tag)
        tags.append(tag)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(X_text)

    model = LogisticRegression(max_iter=500)
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

    print("Pandora NLU treinado e salvo com sucesso.")
    print("Classes:", set(y))


def predict_intent(text: str):
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)

    X = vectorizer.transform([text])
    tag = model.predict(X)[0]
    prob = model.predict_proba(X).max()

    return tag, float(prob)


if __name__ == "__main__":
    print(f"BASE_DIR={BASE_DIR}")
    print(f"DATA_PATH={DATA_PATH} (existe? {DATA_PATH.exists()})")
    train_pandora_model()