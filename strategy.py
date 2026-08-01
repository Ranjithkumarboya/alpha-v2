"""
ALPHA v2
Institutional Strategy Engine
"""

from indicators import Indicators


class StrategyEngine:

    def analyze(self, df):

        if len(df) < 50:
            return {
                "decision": "WAIT",
                "score": 0,
                "reasons": ["Not enough candles"]
            }

        ema20 = Indicators.ema(df, 20)
        ema50 = Indicators.ema(df, 50)

        rsi = Indicators.rsi(df, 14)

        macd, signal = Indicators.macd(df)

        vwap = Indicators.vwap(df)

        upper, lower = Indicators.supertrend(df)

        score = 0
        reasons = []

        # EMA Trend
        if ema20.iloc[-1] > ema50.iloc[-1]:
            score += 20
            reasons.append("EMA Bullish")

        # RSI
        if 55 <= rsi.iloc[-1] <= 70:
            score += 15
            reasons.append("RSI Strong")

        # MACD
        if macd.iloc[-1] > signal.iloc[-1]:
            score += 15
            reasons.append("MACD Bullish")

        # VWAP
        if df["close"].iloc[-1] > vwap.iloc[-1]:
            score += 15
            reasons.append("Above VWAP")

        # Supertrend
        if df["close"].iloc[-1] > upper.iloc[-1]:
            score += 15
            reasons.append("Supertrend Buy")

        # Volume
        avg_vol = df["volume"].rolling(20).mean()

        if df["volume"].iloc[-1] > avg_vol.iloc[-1]:
            score += 20
            reasons.append("Volume Breakout")

        if score >= 80:
            decision = "STRONG BUY"

        elif score >= 60:
            decision = "BUY"

        elif score >= 40:
            decision = "WATCH"

        else:
            decision = "WAIT"

        return {
            "decision": decision,
            "score": score,
            "reasons": reasons
        }
