import os

import streamlit as st

from config.settings import settings
from crew.consulting_crew import create_consulting_crew
from utils.report_formatter import clean_report, report_filename
from utils.ui import inject_css, render_agent_team


st.set_page_config(
    page_title="ConsultIQ — AI Business Consulting Team",
    page_icon="◆",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()

if "report" not in st.session_state:
    st.session_state.report = ""
if "last_brief" not in st.session_state:
    st.session_state.last_brief = ""
if "error" not in st.session_state:
    st.session_state.error = ""

with st.sidebar:
    st.markdown("## CONSULTIQ")
    st.caption("AI-powered business consulting team")
    st.divider()
    st.markdown("### Consulting team")
    render_agent_team()
    st.divider()
    st.caption("Powered by CrewAI + Groq GPT-OSS 120B")

st.markdown(
    '<div class="hero"><h1>Turn a business idea into a strategy.</h1>'
    '<p>A multi-agent consulting team researches the market, customers, competition, business model, and strategy — then audits its own work.</p></div>',
    unsafe_allow_html=True,
)

left, right = st.columns([1.65, 1])

with left:
    st.subheader("Business brief")
    business_brief = st.text_area(
        "Describe the business, product, or opportunity",
        height=190,
        placeholder=(
            "Example: I want to build an AI-powered career coaching platform for university students in Pakistan. "
            "The platform would provide personalized career planning, skill recommendations, and mentor matching."
        ),
        label_visibility="collapsed",
    )

with right:
    st.subheader("Context")
    industry = st.text_input("Industry", placeholder="e.g. EdTech, SaaS, Healthcare")
    geography = st.text_input("Target geography", placeholder="e.g. Pakistan, GCC, Global")
    target_customer = st.text_input("Target customer", placeholder="e.g. University students")

extra_context = f"Industry: {industry or 'Not specified'}\nGeography: {geography or 'Not specified'}\nTarget customer: {target_customer or 'Not specified'}"

st.markdown("### What the team will do")
steps = st.columns(4)
for col, title, desc in zip(
    steps,
    ["Research", "Analyze", "Challenge", "Synthesize"],
    ["Gather current evidence", "Study customers, rivals and economics", "Audit weak assumptions", "Build the final strategy"],
):
    with col:
        st.markdown(f"**{title}**")
        st.caption(desc)

st.divider()

if st.button("Start consulting analysis", type="primary", use_container_width=True):
    if not business_brief.strip():
        st.warning("Please describe the business opportunity first.")
    else:
        try:
            settings.validate()
            os.environ["SERPER_API_KEY"] = settings.serper_api_key
            st.session_state.report = ""
            st.session_state.error = ""
            st.session_state.last_brief = business_brief.strip()

            full_brief = f"{business_brief.strip()}\n\nAdditional context:\n{extra_context}"
            crew = create_consulting_crew()

            with st.status("Consulting team is working...", expanded=True) as status:
                st.write("Researching the market and industry...")
                result = crew.kickoff(inputs={"business_brief": full_brief})
                status.update(label="Consulting analysis complete", state="complete")

            final_text = getattr(result, "raw", None) or str(result)
            st.session_state.report = clean_report(final_text)

        except Exception as exc:
            st.session_state.error = str(exc)
            st.error("The consulting run could not be completed.")
            st.exception(exc)

if st.session_state.error:
    st.info("Check the deployment Secrets and the Streamlit logs if this error persists.")

if st.session_state.report:
    st.divider()
    st.subheader("Business strategy report")
    st.caption("Research-backed synthesis with assumptions and evidence gaps clearly identified.")

    report_tab, team_tab = st.tabs(["Strategy report", "Consulting team"])
    with report_tab:
        st.markdown(st.session_state.report)
        st.download_button(
            "Download Markdown report",
            data=st.session_state.report,
            file_name=report_filename(st.session_state.last_brief),
            mime="text/markdown",
            use_container_width=True,
        )
    with team_tab:
        render_agent_team("Completed")
