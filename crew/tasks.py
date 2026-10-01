from crewai import Task


def build_tasks(agents: dict) -> list[Task]:
    business_researcher = agents["business_researcher"]
    customer_analyst = agents["customer_analyst"]
    competitor_analyst = agents["competitor_analyst"]
    business_analyst = agents["business_analyst"]
    strategy_consultant = agents["strategy_consultant"]
    critical_reviewer = agents["critical_reviewer"]

    research_task = Task(
        description="""
        Research the following business opportunity:

        {business_brief}

        Produce an evidence-led market research memo. Cover:
        1. Industry and market context.
        2. Important recent trends.
        3. Demand or adoption signals.
        4. Opportunity areas.
        5. Constraints and market risks.
        6. A source list with URLs/titles where available.

        Prioritize current and authoritative sources. Mark anything uncertain or estimated.
        """,
        expected_output="A concise, evidence-backed market research memo with source references.",
        agent=business_researcher,
    )

    customer_task = Task(
        description="""
        Analyze customers for this business opportunity:

        {business_brief}

        Cover:
        1. Primary customer segments.
        2. Customer jobs, needs, and pain points.
        3. Current alternatives/workarounds.
        4. Buying or adoption considerations.
        5. Candidate early-adopter segment.
        6. Evidence and uncertainties.

        Use web research. Do not invent customer statistics.
        """,
        expected_output="A customer/problem analysis with segments, pain points, alternatives, evidence, and caveats.",
        agent=customer_analyst,
    )

    competitor_task = Task(
        description="""
        Perform competitive intelligence for:

        {business_brief}

        Identify relevant direct and indirect competitors. For each useful competitor, investigate publicly
        available information on positioning, core offer, target audience, pricing if published, distribution,
        notable strengths, and visible limitations. Then identify possible market gaps.

        Do not fabricate information. Cite sources or label observations as uncertain.
        """,
        expected_output="A competitor landscape and market-gap memo with source references.",
        agent=competitor_analyst,
    )

    business_model_task = Task(
        description="""
        Analyze the business model for:

        {business_brief}

        Use the previous research where relevant. Cover:
        1. Value proposition.
        2. Revenue model options.
        3. Pricing considerations.
        4. Main cost categories.
        5. Illustrative unit-economics formulas or scenarios when useful.
        6. Scalability considerations.
        7. Key financial assumptions and risks.

        Use the calculator for arithmetic. Clearly label all illustrative assumptions.
        """,
        expected_output="A structured business-model and financial-considerations memo with explicit assumptions.",
        agent=business_analyst,
        context=[research_task, customer_task, competitor_task],
    )

    strategy_task = Task(
        description="""
        Act as the senior strategy consultant for:

        {business_brief}

        Synthesize the preceding research into a strategy. Include:
        1. Strategic problem statement.
        2. Target segment and positioning.
        3. Differentiation logic.
        4. Go-to-market approach.
        5. Product/service priorities.
        6. Growth opportunities.
        7. Major risks and mitigations.
        8. A practical 90-day action plan.
        9. Clear assumptions where evidence is incomplete.

        Do not simply repeat the research. Translate evidence into actionable strategic choices.
        """,
        expected_output="A coherent strategy memo grounded in the research and business-model analysis.",
        agent=strategy_consultant,
        context=[research_task, customer_task, competitor_task, business_model_task],
    )

    review_task = Task(
        description="""
        Critically audit the strategy developed for:

        {business_brief}

        Review all preceding work and identify:
        1. Unsupported or weak claims.
        2. Conflicting evidence.
        3. Missing research.
        4. Unrealistic assumptions.
        5. Strategic risks that were overlooked.
        6. Financial/modeling issues.
        7. Specific corrections required before publication.

        Verify important claims with your web research tool when possible.
        """,
        expected_output="A quality-control memo listing issues, evidence concerns, and precise corrections.",
        agent=critical_reviewer,
        context=[research_task, customer_task, competitor_task, business_model_task, strategy_task],
    )

    final_task = Task(
        description="""
        Produce the final consulting report for the following business opportunity:

        {business_brief}

        Use every preceding specialist output and apply the reviewer's corrections. The report must be useful
        to a founder or business decision-maker and must distinguish evidence, assumptions, estimates, and
        strategic recommendations.

        Required structure:
        # Executive Summary
        # Business Opportunity
        # Market Analysis
        # Customer & Problem Analysis
        # Competitive Landscape
        # Business Model & Financial Considerations
        # Strategic Direction
        # Go-To-Market Plan
        # Key Risks & Mitigations
        # 90-Day Action Plan
        # Key Assumptions & Evidence Gaps
        # Sources

        Use concise tables where they improve clarity. Do not invent sources, numbers, or market statistics.
        """,
        expected_output="A polished, evidence-aware business consulting strategy report in Markdown.",
        agent=strategy_consultant,
        context=[
            research_task,
            customer_task,
            competitor_task,
            business_model_task,
            strategy_task,
            review_task,
        ],
    )

    return [
        research_task,
        customer_task,
        competitor_task,
        business_model_task,
        strategy_task,
        review_task,
        final_task,
    ]
