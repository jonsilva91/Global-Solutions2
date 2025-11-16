"""
Orquestrador que decide qual agente responde: Atena, Hygeia, Gaia, Sophia.
"""

from typing import Literal
from src.bot import atenabot, hygeiacheckin
from src.bot.intents_classifier import classify_intent
USER_CONTEXT = {}

Agent = Literal["atena", "hygeia", "gaia", "sophia"]

HELP_TEXT = (
    "📘 **Comandos disponíveis:**\n"
    "- `checkin` – iniciar check-in de bem-estar (Hygeia)\n"
    "- `tarefas` – dicas e automações de trabalho (Atena)\n"
    "- `relatorio` – resumo automático (Atena)\n"
    "- `energia` – informações de sustentabilidade (Gaia)\n"
    "- `inclusao` – métricas de fairness (Sophia)\n"
    "- `ajuda` – mostrar esta lista\n"
    "- `sair` – encerrar bate-papo\n"
)

def route_message(user_id: str, text: str) -> str:
    text = text.lower().strip()

    # comandos globais
    if text in ["ajuda", "help"]:
        return HELP_TEXT

    if text in ["sair", "exit", "quit"]:
        return "Até mais! 👋 Se precisar de mim de novo, é só digitar algo."

    if text in ["voltar", "menu"]:
        return "Voltando ao menu principal...\n\n" + HELP_TEXT

    # classificador de intenção
    intent = classify_intent(text)

    if USER_CONTEXT.get(user_id) == "checkin":
        reply = hygeiacheckin.handle_message(user_id, text)
        if "Obrigado por compartilhar seu estado" in reply:
            USER_CONTEXT[user_id] = None
        return reply
    if intent == "checkin":
        USER_CONTEXT[user_id] = "checkin"
        return hygeiacheckin.handle_message(user_id, text)
    
    
    if intent in ("tarefas", "relatorio"):
        return atenabot.handle_message(user_id, text)

    # futuros:
    if intent == "energia":
        return "🌍 Gaia aqui! Em breve mostrarei insights de energia pelo bot — use o dashboard enquanto isso."

    if intent == "inclusao":
        return "🤝 Sophia aqui! Em breve responderei análises de fairness também."

    # caso não entenda
    return (
        "🤖 Não entendi direito... digite `ajuda` para ver os comandos disponíveis."
    )
