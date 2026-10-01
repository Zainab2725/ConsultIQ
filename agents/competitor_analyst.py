from crewai import Agent
from config.llm import get_llm
from tools.research_tools import web_research_tool


def create_competitor_analyst() -> Agent:
    return Agent(
        role="Competitive Intelligence Analyst",
        goal=(
            "Map direct and indirect competitors, their positioning, offers, pricing when publicly available, "
            "distribution, strengths, weaknesses, and identifiable market gaps."
        ),
        backstory=(
            "You are a competitive intelligence specialist. You investigate competitors with evidence, "
            "distinguish observed facts from interpretation, and never fabricate pricing or product capabilities."
        ),
        tools=[web_research_tool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=8,
    )
