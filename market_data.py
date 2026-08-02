from kiteconnect import KiteConnect
import streamlit as st


class MarketData:

    def __init__(self):
        self.kite = KiteConnect(api_key=st.secrets["API_KEY"])
   if "access_token" in st.session_state:
    self.kite.set_access_token(
        st.session_state["access_token"]
    )
        

    def quote(self, symbol):
        try:
            return self.kite.quote([symbol])[symbol]
        except Exception:
            return None

    def ltp(self, symbol):
        try:
            return self.kite.ltp([symbol])[symbol]["last_price"]
        except Exception:
            return None

    def ohlc(self, symbol):
        try:
            return self.kite.quote([symbol])[symbol]["ohlc"]
        except Exception:
            return None

    def market_status(self):
        try:
            quote = self.kite.quote(["NSE:NIFTY 50"])
            return "OPEN"
        except Exception:
            return "CLOSED"
