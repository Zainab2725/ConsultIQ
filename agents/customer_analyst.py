from crewai import Agent
from config.llm import get_llm
from tools.research_tools import web_research_tool


def create_customer_analyst() -> Agent:
    return Agent(
        role="Customer and Problem Analyst",
        goal=(
            "Determine who the business should serve, what problems those customers experience, "
            "how they solve them today, and which unmet needs may represent opportunities."
        ),
        backstory=(
            "You are a customer strategy consultant skilled in segmentation, customer research, "
            "personas, jobs-to-be-done, and problem validation. You avoid inventing customer facts."
        ),
        tools=[web_research_tool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=8,
    )
