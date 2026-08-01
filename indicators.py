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

        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)

        avg_gain = gain.rolling(period).mean()
        avg_loss = loss.rolling(period).mean()

        rs = avg_gain / avg_loss

        return 100 - (100 / (1 + rs))

    @staticmethod
    def macd(df):
        ema12 = df["close"].ewm(span=12, adjust=False).mean()
        ema26 = df["close"].ewm(span=26, adjust=False).mean()

        macd = ema12 - ema26
        signal = macd.ewm(span=9, adjust=False).mean()

        return macd, signal

    @staticmethod
    def vwap(df):
        tp = (df["high"] + df["low"] + df["close"]) / 3
        return (tp * df["volume"]).cumsum() / df["volume"].cumsum()

    @staticmethod
    def atr(df, period=14):

        high_low = df["high"] - df["low"]
        high_close = abs(df["high"] - df["close"].shift())
        low_close = abs(df["low"] - df["close"].shift())

        tr = pd.concat(
            [high_low, high_close, low_close],
            axis=1
        ).max(axis=1)

        return tr.rolling(period).mean()

    @staticmethod
    def supertrend(df, period=10, multiplier=3):
        atr = Indicators.atr(df, period)

        hl2 = (df["high"] + df["low"]) / 2

        upperband = hl2 + multiplier * atr
        lowerband = hl2 - multiplier * atr

        return upperband, lowerband

    @staticmethod
    def bollinger(df, period=20):
        sma = Indicators.sma(df, period)

        std = df["close"].rolling(period).std()

        upper = sma + 2 * std
        lower = sma - 2 * std

        return upper, lower

    @staticmethod
    def volume_average(df, period=20):
        return df["volume"].rolling(period).mean()
