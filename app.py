"""
====================================================
ALPHA v2.0
Professional Dashboard
====================================================
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_CAPITAL,
    DEFAULT_RISK_PERCENT,
)

from engine import engine
from market import market
from scanner import scanner
from strategy_engine import strategy
from evidence_engine import evidence
from logger import info

# ----------------------------------------
# PAGE CONFIG
# ----------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📈",
    layout="wide",
)

info("ALPHA v2 Started")

# ----------------------------------------
# SIDEBAR
# ----------------------------------------

st.sidebar.title("📈 ALPHA v2")

page = st.sidebar.radio(

    "Navigation",

    [

        "Dashboard",

        "Scanner",

        "Evidence",

        "Strategy",

        "Portfolio",

        "Settings"

    ]

)

# ----------------------------------------
# DASHBOARD
# ----------------------------------------

if page == "Dashboard":

    st.title("📈 ALPHA v2 Dashboard")

    c1, c2, c3 = st.columns(3)

    summary = market.summary()

    with c1:

        st.metric(

            "Market",

            summary["status"]

        )

    with c2:

        st.metric(

            "Capital",

            f"₹{DEFAULT_CAPITAL:,}"

        )

    with c3:

        st.metric(

            "Risk",

            f"{DEFAULT_RISK_PERCENT}%"

        )

    st.divider()

    st.subheader("System Status")

    status = {

        "Engine": "🟢",

        "Market": "🟢",

        "Scanner": "🟢",

        "Strategy": "🟢",

        "Evidence": "🟢",

        "Database": "🟢"

    }

    for k, v in status.items():

        st.write(f"{v} {k}")

    st.divider()

    st.subheader("Today's Decision")

    result = engine.run()

    st.json(result)

# ----------------------------------------
# SCANNER
# ----------------------------------------

elif page == "Scanner":

    st.title("Scanner")

    results = scanner.scan()

    st.dataframe(results)

# ----------------------------------------
# EVIDENCE
# ----------------------------------------

elif page == "Evidence":

    st.title("Evidence")

    symbol = st.text_input("Stock", "RELIANCE")

    if st.button("Check"):

        st.json(

            evidence.recommendation(symbol)

        )

# ----------------------------------------
# STRATEGY
# ----------------------------------------

elif page == "Strategy":

    st.title("Strategy Engine")

    symbol = st.text_input(

        "Stock Name",

        "RELIANCE"

    )

    st.json(

        strategy.evaluate(symbol)

    )

# ----------------------------------------
# PORTFOLIO
# ----------------------------------------

elif page == "Portfolio":

    st.title("Portfolio")

    st.info(

        "Portfolio module coming in next update."

    )

# ----------------------------------------
# SETTINGS
# ----------------------------------------

elif page == "Settings":

    st.title("Settings")

    st.write(

        f"Version : {APP_VERSION}"

    )

    st.write(

        f"Capital : ₹{DEFAULT_CAPITAL:,}"

    )

    st.write(

        f"Risk : {DEFAULT_RISK_PERCENT}%"

    )

st.divider()

st.caption(

    f"{APP_NAME} | Version {APP_VERSION}"

)

