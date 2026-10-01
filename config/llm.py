
from crewai import LLM
from config.settings import settings


def get_llm() -> LLM:
    settings.validate()

    return LLM(
        model=settings.model,
        base_url=settings.groq_base_url,
        api_key=settings.groq_api_key,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
        reasoning_effort="medium",
    )

