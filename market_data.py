from kiteconnect import KiteConnect
import streamlit as st
import pandas as pd


class MarketData:

    def __init__(self):

        self.kite = KiteConnect(
            api_key=st.secrets["API_KEY"]
        )

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

    def instruments(self):

        try:

            data = self.kite.instruments("NFO")

            return pd.DataFrame(data)

        except Exception:

            return pd.DataFrame()

    def nifty_option_chain(self):

        df = self.instruments()

        if df.empty:
            return df

        df = df[
            (df["name"] == "NIFTY") &
            (df["instrument_type"].isin(["CE", "PE"]))
        ]

        return df.sort_values(
            ["expiry", "strike"]
        ).reset_index(drop=True)

    def market_status(self):

        try:

            self.kite.quote(["NSE:NIFTY 50"])

            return "OPEN"

        except Exception:

            return "CLOSED"
