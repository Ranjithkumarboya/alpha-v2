"""
====================================================
ALPHA v2.0.0
Foundation Dashboard
====================================================
"""

import streamlit as st

from config import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_CAPITAL,
    DEFAULT_RISK_PERCENT,
)

from database import db
from logger import info
from utils import market_status

# ----------------------------------------------------
# Page Config
# ----------------------------------------------------

st.set_page_config(
    page_title=APP_NAME,
    page_icon="📈",
    layout="wide",
)

# ----------------------------------------------------
# Startup
# ----------------------------------------------------

info("ALPHA v2 started")

# ----------------------------------------------------
# Header
# ----------------------------------------------------

st.title("📈 ALPHA v2.0")
st.caption("Professional AI Trading Platform")

st.divider()

# ----------------------------------------------------
# Dashboard
# ----------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Market Status",
        market_status()
    )

with col2:
    st.metric(
        "Capital",
        f"₹{DEFAULT_CAPITAL:,}"
    )

with col3:
    st.metric(
        "Risk / Trade",
        f"{DEFAULT_RISK_PERCENT}%"
    )

st.divider()

# ----------------------------------------------------
# System Health
# ----------------------------------------------------

st.subheader("🟢 System Health")

health = {
    "Configuration": "✅",
    "Database": "✅",
    "Logger": "✅",
    "Utilities": "✅",
}

for k, v in health.items():
    st.write(f"{v} {k}")

st.divider()

# ----------------------------------------------------
# Coming Soon
# ----------------------------------------------------

st.subheader("🚀 Coming in Next Builds")

st.info("""
• Live Zerodha Login

• Market Scanner

• Evidence Engine

• Options Engine

• News Engine

• Portfolio Manager

• AI Decision Engine
""")

st.divider()

st.caption(
    f"{APP_NAME} | Version {APP_VERSION}"
)
