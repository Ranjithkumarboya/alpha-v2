"""
=========================================
ALPHA v2
Professional Market Data Engine
=========================================
"""

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

            df = pd.DataFrame(
                self.kite.instruments("NFO")
            )

            return df

        except Exception:

            return pd.DataFrame()

    def nifty_option_chain(self):

        df = self.instruments()
        st.write("========== DEBUG ==========")
        st.write("Total Instruments:", len(df))
        st.write("Columns:", list(df.columns))
        st.dataframe(df.head(20))

        if df.empty:

            return pd.DataFrame()

        required = [
            "segment",
            "name",
            "instrument_type",
            "expiry",
            "strike",
            "tradingsymbol"
        ]

        for col in required:

            if col not in df.columns:

                return pd.DataFrame()

        df = df[
            (df["segment"] == "NFO-OPT") &
            (df["name"] == "NIFTY") &
            (df["instrument_type"].isin(["CE", "PE"]))
        ].copy()
        st.write("Filtered Instruments:", len(df))
        st.dataframe(df.head(20))
        st.write("===========================")

        if df.empty:

            return pd.DataFrame()

        df["expiry"] = pd.to_datetime(
            df["expiry"]
        )

        df["strike"] = df["strike"].astype(float)

        df = df.sort_values(
            ["expiry", "strike"]
        )
        st.write(df["instrument_type"].value_counts())

        st.write(df.head(20))

        return df.reset_index(drop=True)

    def market_status(self):

        try:

            self.kite.quote(
                ["NSE:NIFTY 50"]
            )

            return "OPEN"

        except Exception:

            return "CLOSED"


market_data = MarketData()
