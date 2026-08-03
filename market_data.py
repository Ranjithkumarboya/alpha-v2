"""
=========================================
ALPHA v2
Professional Market Data Engine
=========================================
"""

import streamlit as st
import pandas as pd

from kite_session import KiteSession


class MarketData:

    def __init__(self):
        self.refresh_session()

    def refresh_session(self):
        self.kite = KiteSession.get_kite()

    def quote(self, symbol):

        self.refresh_session()

        try:
            return self.kite.quote([symbol])[symbol]

        except Exception as e:
            st.error(e)
            return None

    def ltp(self, symbol):

        self.refresh_session()

        try:
            return self.kite.ltp([symbol])[symbol]["last_price"]

        except Exception as e:
            st.error(e)
            return None

    def ohlc(self, symbol):

        self.refresh_session()

        try:
            return self.kite.quote([symbol])[symbol]["ohlc"]

        except Exception as e:
            st.error(e)
            return None

    def instruments(self):

        self.refresh_session()

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

        if df.empty:
            return pd.DataFrame()

        df["expiry"] = pd.to_datetime(df["expiry"])
        df["strike"] = df["strike"].astype(float)

        return df.sort_values(
            ["expiry", "strike"]
        ).reset_index(drop=True)

    def historical_data(
        self,
        instrument_token,
        from_date,
        to_date,
        interval="5minute"
    ):

        self.refresh_session()

        try:

            data = self.kite.historical_data(
                instrument_token=instrument_token,
                from_date=from_date,
                to_date=to_date,
                interval=interval
            )

            return pd.DataFrame(data)

        except Exception as e:

            st.error(e)
            return pd.DataFrame()

    def market_status(self):

        self.refresh_session()

        try:
            self.kite.quote(["NSE:NIFTY 50"])
            return "OPEN"

        except Exception:
            return "CLOSED"


market_data = MarketData()
