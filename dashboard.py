"""
ALPHA v2
Dashboard Module
"""

import streamlit as st


class Dashboard:

    def header(self):

        st.title("📈 ALPHA v2")

        st.caption("Professional AI Trading Platform")

    def market_status(self, status):

        if status:

            st.success("🟢 Market Open")

        else:

            st.error("🔴 Market Closed")

    def show_trade(self, result):

        st.subheader(result["symbol"])

        c1, c2 = st.columns(2)

        with c1:

            st.metric("Decision", result["action"])

            st.metric("Confidence", f'{result["confidence"]}%')

            st.metric("Score", result["score"])

        with c2:

            st.metric("Entry", result["entry"])

            st.metric("Stoploss", result["stoploss"])

            st.metric("Target 1", result["target1"])

            st.metric("Target 2", result["target2"])

        st.write("### Evidence")

        for reason in result["reasons"]:

            st.success(reason)
