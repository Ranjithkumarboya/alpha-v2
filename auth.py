from kiteconnect import KiteConnect
import streamlit as st


class ZerodhaAuth:

    def __init__(self):
        self.kite = KiteConnect(api_key=st.secrets["API_KEY"])

    def login_url(self):
        return self.kite.login_url()

    def generate_session(self, request_token):

        data = self.kite.generate_session(
            request_token,
            api_secret=st.secrets["API_SECRET"]
        )

        self.kite.set_access_token(data["access_token"])

        return data["access_token"]
