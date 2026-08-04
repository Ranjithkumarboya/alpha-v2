"""
=========================================
ALPHA v2
Professional Analysis Engine
Version 2.0
=========================================
"""

from datetime import datetime, timedelta
from market_data import MarketData
from indicators import Indicators


class AnalysisEngine:

    def __init__(self):
        self.market = MarketData()

    def historical_candles(self):
        to_date = datetime.now()
        from_date = to_date - timedelta(days=5)
        return self.market.historical_by_symbol(
            exchange="NSE",
            tradingsymbol="NIFTY 50",
            from_date=from_date,
            to_date=to_date,
            interval="5minute"
        )

    def analyze(self):
        df = self.historical_candles()

        if df.empty or len(df) < 60:
            return {
                "status":"FAILED",
                "message":"Historical candles not available"
            }

        df=df.copy()
        df["EMA20"]=Indicators.ema(df,20)
        df["EMA50"]=Indicators.ema(df,50)
        df["RSI"]=Indicators.rsi(df,14)
        macd,signal=Indicators.macd(df)
        df["MACD"]=macd
        df["MACD_SIGNAL"]=signal
        df["VWAP"]=Indicators.vwap(df)
        df["ATR"]=Indicators.atr(df,14)

        last=df.iloc[-1]

        trend="SIDEWAYS"
        signal_text="WAIT"
        confidence=50

        if last["EMA20"]>last["EMA50"]:
            trend="BULLISH"
            signal_text="BUY CE"
            confidence+=20
        elif last["EMA20"]<last["EMA50"]:
            trend="BEARISH"
            signal_text="BUY PE"
            confidence+=20

        if last["RSI"]>60 or last["RSI"]<40:
            confidence+=15

        if last["MACD"]>last["MACD_SIGNAL"]:
            confidence+=20
        else:
            confidence+=10

        if last["close"]>last["VWAP"]:
            confidence+=15

        confidence=min(95,int(confidence))

        return {
            "status":"SUCCESS",
            "Spot":round(float(last["close"]),2),
            "Trend":trend,
            "Signal":signal_text,
            "Confidence":confidence,
            "EMA20":round(float(last["EMA20"]),2),
            "EMA50":round(float(last["EMA50"]),2),
            "RSI":round(float(last["RSI"]),2),
            "MACD":round(float(last["MACD"]),2),
            "MACD_SIGNAL":round(float(last["MACD_SIGNAL"]),2),
            "VWAP":round(float(last["VWAP"]),2),
            "ATR":round(float(last["ATR"]),2)
        }

    def summary(self):
        return self.analyze()


analysis=AnalysisEngine()
