from app.services.llm_service import LLMService


service = LLMService()

answer = service.ask("What is revenue?")

print(answer)