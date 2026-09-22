from langchain_core.messages import SystemMessage, HumanMessage

from agent.llm import create_llm
from agent.prompts import SYSTEM_PROMPT


class MetricMindAgent:
    """Basic MetricMind-AI agent for understanding analytics questions."""

    def __init__(self):
        self.llm = create_llm()

    def ask(self, question: str) -> str:
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=question),
        ]

        response = self.llm.invoke(messages)

        return response.content