import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    model: str = os.getenv("MODEL_NAME", "gemini/gemini-2.5-flash")
    temperature: float = float(os.getenv("MODEL_TEMPERATURE", "0.2"))
    max_tokens: int = int(os.getenv("MAX_OUTPUT_TOKENS", "6000"))

    @property
    def gemini_api_key(self) -> str:
        return os.getenv("GEMINI_API_KEY", "")

    @property
    def serper_api_key(self) -> str:
        return os.getenv("SERPER_API_KEY", "")

    def validate(self) -> None:
        missing = []

        if not self.gemini_api_key:
            missing.append("GEMINI_API_KEY")

        if not self.serper_api_key:
            missing.append("SERPER_API_KEY")

        if missing:
            raise RuntimeError(
                "Missing Streamlit secrets/environment variables: "
                + ", ".join(missing)
            )


settings = Settings()
