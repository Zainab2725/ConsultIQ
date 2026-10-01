from crewai import Crew, Process

from agents.business_researcher import create_business_researcher
from agents.customer_analyst import create_customer_analyst
from agents.competitor_analyst import create_competitor_analyst
from agents.business_analyst import create_business_analyst
from agents.strategy_consultant import create_strategy_consultant
from agents.critical_reviewer import create_critical_reviewer
from crew.tasks import build_tasks


def create_consulting_crew() -> Crew:
    agents = {
        "business_researcher": create_business_researcher(),
        "customer_analyst": create_customer_analyst(),
        "competitor_analyst": create_competitor_analyst(),
        "business_analyst": create_business_analyst(),
        "strategy_consultant": create_strategy_consultant(),
        "critical_reviewer": create_critical_reviewer(),
    }

    tasks = build_tasks(agents)

    return Crew(
        agents=list(agents.values()),
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
        memory=False,
    )
