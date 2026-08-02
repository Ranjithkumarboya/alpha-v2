"""
=========================================
ALPHA v2
Professional AI Trading Platform
=========================================
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from kite_login import KiteLogin
from dashboard import dashboard
from market import market
from market_data import market_data
from option_chain import option_chain
from scanner import scanner
from ai_engine import ai

st.set_page_config(
    page_title="ALPHA v2",
    page_icon="🚀",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="market_refresh"
)

dashboard.header()

tab1, tab2, tab3, tab4 = st.tabs([
    "Dashboard",
    "Scanner",
    "AI",
    "Login"
])

# =====================================================
# DASHBOARD
# =====================================================

with tab1:

    summary = market.summary()

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Market",
        summary["status"]
    )

    c2.metric(
        "Market Regime",
        summary["regime"]
    )

    c3.metric(
        "Expiry",
        summary["expiry"]
    )

    st.divider()

    if "access_token" not in st.session_state:

        st.warning(
            "Please login to Zerodha to view live market data."
        )

    else:

        st.subheader("📈 Live Market")

        col1, col2 = st.columns(2)

        col1.metric(
            "NIFTY 50",
            market_data.ltp("NSE:NIFTY 50")
        )

        col2.metric(
            "BANK NIFTY",
            market_data.ltp("NSE:NIFTY BANK")
        )

        st.divider()

        st.subheader("📈 ATM Option Chain")

        option = option_chain.summary()

        if option is None:

            st.error(
                "Unable to load Option Chain."
            )

        else:

            st.write(
                f"ATM Strike : {option['strike']}"
            )

            c3, c4 = st.columns(2)

            c3.metric(
                "CE Premium",
                option["ce_price"]
            )

            c4.metric(
                "PE Premium",
                option["pe_price"]
            )

            st.write(
                f"CE Symbol : {option['ce_symbol']}"
            )

            st.write(
                f"PE Symbol : {option['pe_symbol']}"
            )

    st.divider()

# =====================================================
# SCANNER
# =====================================================

with tab2:

    st.subheader("📊 Scanner")

    scan = scanner.scan()

    st.dataframe(
        scan,
        use_container_width=True
    )

# =====================================================
# AI
# =====================================================

with tab3:

    st.subheader("🤖 AI Decision Engine")

    data = ai.summary()

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

# =====================================================
# LOGIN
# =====================================================

with tab4:

    if "access_token" in st.session_state:

        st.success("✅ Zerodha Connected")

    else:

        login = KiteLogin()

        login.login()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "🚀 ALPHA v2 | Professional AI Trading Platform"
)
