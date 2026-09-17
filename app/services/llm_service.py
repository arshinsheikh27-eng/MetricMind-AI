import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class LLMService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(api_key=api_key, timeout=20.0)

    def ask(self, question: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are MetricMind AI, a business analytics assistant. "
                        "Answer the user's business question clearly and concisely. "
                        "Do not invent numerical data. "
                        "If actual database data is not provided, explain that."
                    ),
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        return response.output_text