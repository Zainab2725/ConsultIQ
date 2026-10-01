import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("MODEL_NAME", "openai/gpt-oss-120b")
    groq_base_url: str = "https://api.groq.com/openai/v1"
    temperature: float = float(os.getenv("MODEL_TEMPERATURE", "0.2"))
    max_tokens: int = int(os.getenv("MAX_OUTPUT_TOKENS", "6000"))

    @property
    def groq_api_key(self) -> str:
        return os.getenv("GROQ_API_KEY", "")

    @property
    def serper_api_key(self) -> str:
        return os.getenv("SERPER_API_KEY", "")

    def validate(self) -> None:
        missing = []
        if not self.groq_api_key:
            missing.append("GROQ_API_KEY")
        if not self.serper_api_key:
            missing.append("SERPER_API_KEY")
        if missing:
            raise RuntimeError(
                "Missing Streamlit secrets/environment variables: " + ", ".join(missing)
            )


settings = Settings()
