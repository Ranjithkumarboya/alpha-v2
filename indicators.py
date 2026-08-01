"""
ALPHA v2
Technical Indicators Engine
"""

import pandas as pd


class Indicators:

    @staticmethod
    def ema(df, period=20):
        return df["close"].ewm(span=period, adjust=False).mean()

    @staticmethod
    def sma(df, period=20):
        return df["close"].rolling(period).mean()

    @staticmethod
    def rsi(df, period=14):

        delta = df["close"].diff()

        gain = delta.clip(lower=0)

        loss = -delta.clip(upper=0)

        avg_gain = gain.rolling(period).mean()

        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))

    @staticmethod
    def macd(df):

        ema12 = df["close"].ewm(span=12).mean()

        ema26 = df["close"].ewm(span=26).mean()

        macd = ema12 - ema26

        signal = macd.ewm(span=9).mean()

        return macd, signal

    @staticmethod
    def vwap(df):

        tp = (df["high"] + df["low"] + df["close"]) / 3

        return (tp * df["volume"]).cumsum() / df["volume"].cumsum()

    @staticmethod
    def atr(df, period=14):

        hl = df["high"] - df["low"]

        hc = abs(df["high"] - df["close"].shift())

        lc = abs(df["low"] - df["close"].shift())

        tr = pd.concat([hl, hc, lc], axis=1).max(axis=1)

        return tr.rolling(period).mean()

    @staticmethod
    def supertrend(df, period=10, multiplier=3):

        atr = Indicators.atr(df, period)

        hl2 = (df["
