"""
ALPHA v2
Integrated Dashboard
"""

from kite_login import KiteLogin
import streamlit as st
from streamlit_autorefresh import st_autorefresh

from market import market
from market_data import MarketData
from option_chain import OptionChain
from scanner import scanner
from ai_engine import AIEngine
from dashboard import Dashboard

st.set_page_config(
    page_title="ALPHA v2",
    page_icon="📈",
    layout="wide"
)

st_autorefresh(
    interval=5000,
    key="market_refresh"
)

dashboard = Dashboard()
ai = AIEngine()
market_data = MarketData()
option_chain = OptionChain()

dashboard.header()

tab1, tab2, tab3, tab4 = st.tabs([
    "Dashboard",
    "Scanner",
    "AI",
    "Login"
])

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

    st.divider()

    if "access_token" in st.session_state:

        st.subheader("📈 Live Market")

        nifty = market_data.ltp("NSE:NIFTY 50")
        banknifty = market_data.ltp("NSE:NIFTY BANK")

        col1, col2 = st.columns(2)

        col1.metric("NIFTY 50", nifty)
        col2.metric("BANK NIFTY", banknifty)

        st.divider()

        st.subheader("📈 ATM Option Chain")

        strike = option_chain.atm_strike()
symbols = option_chain.option_symbols()
prices = option_chain.option_prices()

st.write(f"ATM Strike : {strike}")

col1, col2 = st.columns(2)

col1.metric(
    "CE Premium",
    prices["CE"]
)

col2.metric(
    "PE Premium",
    prices["PE"]
)

st.write(f"CE Symbol : {symbols['CE']}")
st.write(f"PE Symbol : {symbols['PE']}")

    else:
        st.warning("Login to Zerodha to view Live Market Data")


with tab2:

    st.subheader("Scanner")

    data = scanner.scan()

    st.dataframe(data)


with tab3:

    st.subheader("AI Decision")

    st.info(
        "AI module will evaluate live market data in next update."
    )


with tab4:

    if "access_token" in st.session_state:
        st.success("✅ Zerodha Connected")
    else:
        login = KiteLogin()
        login.login()


st.divider()

st.caption("ALPHA v2")
