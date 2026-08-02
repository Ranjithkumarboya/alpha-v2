from kiteconnect import KiteConnect
import streamlit as st
import pandas as pd


class MarketData:

    def __init__(self):
        self.kite = KiteConnect(
            api_key=st.secrets["API_KEY"]
        )

    def connect(self):
        if "access_token" in st.session_state:
            self.kite.set_access_token(
                st.session_state["access_token"]
            )

    def quote(self, symbol):

        self.connect()

        try:
            return self.kite.quote([symbol])[symbol]
        except Exception as e:
            st.error(e)
            return None

    def ltp(self, symbol):

        self.connect()

        try:
            return self.kite.ltp([symbol])[symbol]["last_price"]
        except Exception as e:
            st.error(e)
            return None

    def ohlc(self, symbol):

        self.connect()

        try:
            return self.kite.quote([symbol])[symbol]["ohlc"]
        except Exception as e:
            st.error(e)
            return None

    def instruments(self):

        self.connect()

        try:
            return pd.DataFrame(
                self.kite.instruments("NFO")
            )
        except Exception as e:
            st.error(e)
            return pd.DataFrame()

    def nifty_option_chain(self):

        df = self.instruments()

        if df.empty:
            return pd.DataFrame()

        df = df[
            (df["segment"] == "NFO-OPT") &
            (df["name"] == "NIFTY") &
            (df["instrument_type"].isin(["CE", "PE"]))
        ].copy()

        if df.empty:
            return pd.DataFrame()

        df["expiry"] = pd.to_datetime(df["expiry"])
        df["strike"] = df["strike"].astype(float)

        return df.sort_values(
            ["expiry", "strike"]
        ).reset_index(drop=True)

    def market_status(self):

        self.connect()

        try:
            self.kite.quote(["NSE:NIFTY 50"])
            return "OPEN"
        except:
            return "CLOSED"


market_data = MarketData()
