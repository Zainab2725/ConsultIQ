```python
from crewai.tools import tool


@tool("Business Calculator")
def calculator(expression: str) -> str:
    """
    Calculate a basic mathematical expression for business analysis.

    Use this tool for arithmetic such as:
    - 1000 * 0.20
    - 50000 / 1000
    - (120 - 80) / 80 * 100
    - 100 * 12

    Only mathematical expressions should be provided.
    """

    try:
        # Allow only characters needed for basic arithmetic.
        allowed = set("0123456789+-*/().,% ")

        cleaned = expression.replace("%", "/100")

        if not set(cleaned) <= allowed:
            return "Invalid expression. Use numbers and basic arithmetic operators only."

        result = eval(cleaned, {"__builtins__": {}}, {})

        return f"Result: {result}"

    except Exception as exc:
        return f"Could not calculate expression: {exc}"


def calculator_tool():
    return calculator
```
