from crewai import Agent
from config.llm import get_llm
from tools.research_tools import web_research_tool


def create_business_researcher() -> Agent:
    return Agent(
        role="Senior Business Research Analyst",
        goal=(
            "Research the client's business opportunity using current, relevant external evidence. "
            "Identify market conditions, industry trends, demand signals, opportunities, and constraints."
        ),
        backstory=(
            "You are a consulting research analyst who separates evidence from assumptions. "
            "You prefer recent primary or authoritative sources, cross-check important claims, "
            "and clearly identify uncertainty."
        ),
        tools=[web_research_tool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=8,
    )
