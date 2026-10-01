from crewai import LLM
from config.settings import settings


def get_llm() -> LLM:
    settings.validate()

    return LLM(
        model=settings.model,
        api_key=settings.gemini_api_key,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
    )
