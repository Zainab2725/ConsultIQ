# ConsultIQ — AI Business Consulting Team

ConsultIQ is a Streamlit business-consulting workspace powered by a CrewAI multi-agent team and Groq's `openai/gpt-oss-120b` model.

The team researches a business opportunity, analyzes customers and competitors, examines the business model, develops strategy, performs a critical review, and produces a structured consulting report.

## Architecture

Six specialized agents:

1. **Business Researcher** — market and industry research
2. **Customer Analyst** — customer segments, problems and adoption
3. **Competitor Analyst** — competitive intelligence and gaps
4. **Business Analyst** — business model and financial considerations
5. **Strategy Consultant** — positioning, go-to-market and 90-day plan
6. **Critical Reviewer** — evidence and strategy quality control

The workflow is sequential so each specialist can consume earlier findings before the final report is synthesized.

## Tools

Agents use CrewAI Tools:

- `SerperDevTool` for web research
- `CalculatorTool` for quantitative calculations

The web research key is kept outside the repository.

## Project structure

```text
business-consulting-ai/
├── app.py
├── agents/
│   ├── business_researcher.py
│   ├── customer_analyst.py
│   ├── competitor_analyst.py
│   ├── business_analyst.py
│   ├── strategy_consultant.py
│   └── critical_reviewer.py
├── crew/
│   ├── consulting_crew.py
│   └── tasks.py
├── tools/
│   ├── research_tools.py
│   └── analysis_tools.py
├── config/
│   ├── settings.py
│   └── llm.py
├── utils/
│   ├── report_formatter.py
│   └── ui.py
├── requirements.txt
├── runtime.txt
├── .gitignore
└── README.md
```

## Streamlit Secrets

In Streamlit Community Cloud, add:

```toml
GROQ_API_KEY = "your-groq-key"
SERPER_API_KEY = "your-serper-key"
```

Do not commit secrets to GitHub.

## GitHub → Streamlit deployment

1. Create a GitHub repository.
2. Upload the project files and folders.
3. Open Streamlit Community Cloud.
4. Choose **Create app** and select your GitHub repository.
5. Select `app.py` as the entry point.
6. Use Python 3.12.
7. Open **Advanced settings → Secrets** and paste the two secrets.
8. Deploy.

You do not need to install Python, CrewAI, or Streamlit locally for this GitHub-to-Streamlit workflow.

## Important notes

- The app does not hard-code API keys.
- Research claims should be checked against the cited sources before making important real-world decisions.
- Financial figures are treated as assumptions or scenarios unless supported by evidence.
- The system is designed as a decision-support tool, not a substitute for professional legal, financial, tax, or investment advice.
