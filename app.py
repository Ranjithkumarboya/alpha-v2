"""
ALPHA v2
Integrated Dashboard
"""

import streamlit as st

from market import market
from scanner import scanner
from ai_engine import AIEngine
from dashboard import Dashboard

st.set_page_config(
    page_title="ALPHA v2",
    page_icon="📈",
    layout="wide"
)

dashboard = Dashboard()
ai = AIEngine()

dashboard.header()

tab1, tab2, tab3 = st.tabs(
    [
        "Dashboard",
        "Scanner",
        "AI"
    ]
)

with tab1:

    summary = market.summary()

    st.metric(
        "Market",
        summary["status"]
    )

    st.metric(
        "Market Regime",
        summary["regime"]
    )

    st.metric(
        "Expiry",
        str(summary["expiry"])
    )

with tab2:

    st.subheader("Scanner")

    data = scanner.scan()

    st.dataframe(data)

with tab3:

    st.subheader("AI Decision")

    st.info(
        "AI module will evaluate live market data in next update."
    )

st.divider()

st.caption("ALPHA v2")
