"""
Alpha v2
Zerodha Integration
"""

from kiteconnect import KiteConnect
import streamlit as st

class Zerodha:

    def __init__(self):
        self.api_key = st.secrets.get("API_KEY", "")
        self.api_secret = st.secrets.get("API_SECRET", "")
        self.redirect_url = st.secrets.get("REDIRECT_URL", "")

        self.kite = KiteConnect(api_key=self.api_key)

    def login_url(self):
        return self.kite.login_url()

    def create_session(self, request_token):
        data = self.kite.generate_session(
            request_token=request_token,
            api_secret=self.api_secret,
        )

        access_token = data["access_token"]

        self.kite.set_access_token(access_token)

        return access_token

    def profile(self):
        return self.kite.profile()

    def margins(self):
        return self.kite.margins()

    def holdings(self):
        return self.kite.holdings()

    def positions(self):
        return self.kite.positions()

    def orders(self):
        return self.kite.orders()

    def quotes(self, symbols):
        return self.kite.quote(symbols)

    def ltp(self, symbols):
        return self.kite.ltp(symbols)


zerodha = Zerodha()
