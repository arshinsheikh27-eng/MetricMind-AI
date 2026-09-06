import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from ai.prompts.system_prompt import SYSTEM_PROMPT

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

question = "Show European sales."

response = llm.invoke([
    ("system", SYSTEM_PROMPT),
    ("human", question)
])

print(response.content)