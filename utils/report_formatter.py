import re


def clean_report(text: str) -> str:
    """Remove accidental wrapper fences while preserving normal Markdown."""
    if not text:
        return "No report was returned."
    cleaned = text.strip()
    cleaned = re.sub(r"^```(?:markdown|md)?\s*", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"\s*```$", "", cleaned)
    return cleaned.strip()


def report_filename(business_name: str) -> str:
    safe = re.sub(r"[^a-zA-Z0-9]+", "-", business_name).strip("-").lower()
    return f"{safe or 'business'}-strategy-report.md"
