"""
Classificador simples de intenção baseado em palavras-chave.
"""

from typing import Literal

Intent = Literal["checkin", "energia", "tarefas", "relatorio", "outro"]

def classify_intent(text: str) -> Intent:
    t = text.lower()
    if "checkin" in t or "como estou" in t:
        return "checkin"
    if "energia" in t or "luz" in t or "kwh" in t:
        return "energia"
    if "tarefas" in t or "to-do" in t or "prioridade" in t:
        return "tarefas"
    if "relatorio" in t or "report" in t:
        return "relatorio"
    return "outro"
