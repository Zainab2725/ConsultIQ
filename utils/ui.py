import streamlit as st


def inject_css() -> None:
    st.markdown(
        """
        <style>
        .stApp { background: #f7f5f0; }
        .block-container { max-width: 1180px; padding-top: 2rem; padding-bottom: 4rem; }
        .hero {
            padding: 2.2rem 2.4rem;
            border-radius: 24px;
            background: linear-gradient(135deg, #171321 0%, #302354 100%);
            color: white;
            margin-bottom: 1.5rem;
        }
        .hero h1 { margin: 0 0 .5rem 0; font-size: 2.7rem; letter-spacing: -1px; }
        .hero p { margin: 0; color: #ddd6ee; font-size: 1.05rem; }
        .agent-card {
            border: 1px solid #e4dfd4;
            border-radius: 16px;
            padding: 1rem 1.1rem;
            background: #fffdf9;
            margin-bottom: .7rem;
        }
        .agent-title { font-weight: 700; color: #29242f; }
        .agent-desc { color: #6e6875; font-size: .9rem; }
        .section-card {
            border: 1px solid #e4dfd4;
            border-radius: 18px;
            padding: 1.3rem;
            background: #fffdf9;
        }
        div.stButton > button[kind="primary"] {
            background: #7254c8;
            border-color: #7254c8;
            color: white;
            border-radius: 12px;
            padding: .7rem 1.2rem;
            font-weight: 700;
        }
        div.stButton > button[kind="primary"]:hover { background: #5d40b3; border-color: #5d40b3; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_agent_team(status: str = "Ready") -> None:
    agents = [
        ("Market Researcher", "Market, industry and demand evidence"),
        ("Customer Analyst", "Segments, pain points and adoption"),
        ("Competitor Analyst", "Competitors, positioning and gaps"),
        ("Business Analyst", "Revenue, costs and business model"),
        ("Strategy Consultant", "Positioning, GTM and priorities"),
        ("Critical Reviewer", "Evidence and strategy quality control"),
    ]
    for name, desc in agents:
        st.markdown(
            f'<div class="agent-card"><div class="agent-title">{name}</div>'
            f'<div class="agent-desc">{desc} · {status}</div></div>',
            unsafe_allow_html=True,
        )
