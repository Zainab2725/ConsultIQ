from crewai import Agent
from config.llm import get_llm
from tools.research_tools import web_research_tool


def create_strategy_consultant() -> Agent:
    return Agent(
        role="Senior Strategy Consultant",
        goal=(
            "Turn the research into a coherent business strategy: positioning, differentiation, "
            "go-to-market approach, strategic priorities, growth opportunities, risks, and a practical 90-day plan."
        ),
        backstory=(
            "You are a senior strategy consultant who synthesizes evidence from multiple specialists. "
            "You do not invent missing facts. Recommendations must trace back to research, assumptions, "
            "or clearly labeled strategic judgment."
        ),
        tools=[web_research_tool()],
        llm=get_llm(),
        verbose=True,
        allow_delegation=False,
        max_iter=8,
    )
