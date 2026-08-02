from kiteconnect import KiteConnect
import streamlit as st


class OptionChain:

    def __init__(self):
        self.kite = KiteConnect(api_key=st.secrets["API_KEY"])

        if "access_token" in st.session_state:
            self.kite.set_access_token(
                st.session_state["access_token"]
            )

    def ltp(self):
        try:
            return self.kite.ltp(["NSE:NIFTY 50"])["NSE:NIFTY 50"]["last_price"]
        except Exception:
            return None

    def atm_strike(self):

        ltp = self.ltp()

        if ltp is None:
            return None

        return round(ltp / 50) * 50

    def current_expiry(self):
        return "AUTO"

    def option_symbols(self):

        strike = self.atm_strike()

        expiry = self.current_expiry()

        return {
            "CE": f"NFO:NIFTY{expiry}{strike}CE",
            "PE": f"NFO:NIFTY{expiry}{strike}PE"
        }
