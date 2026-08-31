import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class LLMService:
    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")

        self.client = OpenAI(api_key=api_key)

    def ask(self, question: str) -> str:
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=question,
        )

        return response.output_text