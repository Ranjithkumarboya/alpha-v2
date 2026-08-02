"""
=========================================
ALPHA v2
Professional Dashboard
=========================================
"""

import streamlit as st

from ai_engine import ai
from option_chain import option_chain
from market import market


class Dashboard:

    def __init__(self):
        pass

    def header(self):

        st.title("🚀 ALPHA v2")

        st.caption(
            "AI Powered Options Trading Platform"
        )

    def market_summary(self):

        summary = market.summary()

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Market",
            summary["status"]
        )

        c2.metric(
            "Trend",
            summary["regime"]
        )

        c3.metric(
            "Expiry",
            summary["expiry"]
        )

    def option_summary(self):

        data = option_chain.summary()

        st.subheader("📈 ATM Option Chain")

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Spot",
            data["spot"]
        )

        c2.metric(
            "ATM",
            data["strike"]
        )

        c3.metric(
            "CE Premium",
            data["ce_price"]
        )

        c4, c5 = st.columns(2)

        c4.metric(
            "PE Premium",
            data["pe_price"]
        )

        st.write(
            "CE :", data["ce_symbol"]
        )

        st.write(
            "PE :", data["pe_symbol"]
        )

    def ai_summary(self):

        data = ai.summary()

        st.subheader("🤖 AI Decision")

        c1, c2 = st.columns(2)

        c1.metric(
            "Action",
            data["Action"]
        )

        c2.metric(
            "Confidence",
            f"{data['Confidence']}%"
        )

        c3, c4 = st.columns(2)

        c3.metric(
            "Trend",
            data["Trend"]
        )

        c4.metric(
            "Risk",
            data["Risk"]
        )


dashboard = Dashboard()
