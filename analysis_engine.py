
"""
=========================================
ALPHA v2
Professional Analysis Engine
Version 1
=========================================
"""

from datetime import datetime, timedelta

import pandas as pd

from market_data import MarketData


class AnalysisEngine:

    def __init__(self):

        self.market = MarketData()

    def historical_candles(self):

        to_date = datetime.now()

        from_date = to_date - timedelta(days=5)

        df = self.market.historical_by_symbol(
            exchange="NSE",
            tradingsymbol="NIFTY 50",
            from_date=from_date,
            to_date=to_date,
            interval="5minute"
        )

        return df

    def summary(self):

        df = self.historical_candles()

        if df.empty:

            return {

                "status": "FAILED",

                "message": "Historical candles not available"

            }

        last = df.iloc[-1]

        return {

            "status": "SUCCESS",

            "candles": len(df),

            "last_close": float(last["close"]),

            "last_high": float(last["high"]),

            "last_low": float(last["low"]),

            "last_volume": int(last["volume"])

        }


analysis = AnalysisEngine()
