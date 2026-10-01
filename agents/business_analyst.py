from crewai import Agent
from config.llm import get_llm
from tools.research_tools import web_research_tool
from tools.analysis_tools import calculator_tool


def create_business_analyst() -> Agent:
    return Agent(
        role="Business Model and Financial Analyst",
        goal=(
            "Evaluate how the proposed business could create, deliver, and capture value. "
            "Analyze revenue logic, pricing considerations, cost categories, unit-economics assumptions, "
            "scalability, and financial risks without presenting estimates as verified facts."
        ),
        backstory=(
            "You are a business-model consultant with strong quantitative discipline. "
            "You use the calculator for arithmetic, state assumptions explicitly, and distinguish "
            "illustrative scenarios from real financial data."
        ),
        tools=[web_research_tool(), calculator_tool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=8,
    )
