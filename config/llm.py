from crewai import LLM
from config.settings import settings


def get_llm() -> LLM:
    """Create the Groq GPT-OSS 120B LLM through Groq's OpenAI-compatible API."""
    return LLM(
        model=settings.model,
        base_url=settings.groq_base_url,
        api_key=settings.groq_api_key,
        temperature=settings.temperature,
        max_tokens=settings.max_tokens,
        reasoning_effort="medium",
    )
