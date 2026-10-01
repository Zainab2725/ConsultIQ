from crewai_tools import SerperDevTool


def web_research_tool():
    """CrewAI web search tool backed by Serper."""
    return SerperDevTool()
