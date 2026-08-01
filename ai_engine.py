"""
ALPHA v2
AI Evidence Engine
"""

from strategy import StrategyEngine


class AIEngine:

    def __init__(self):
        self.strategy = StrategyEngine()

    def evaluate(self, symbol, df):

        result = self.strategy.analyze(df)

        score = result["score"]

        confidence = min(99, score)

        if score >= 80:
            action = "STRONG BUY"

        elif score >= 60:
            action = "BUY"

        elif score >= 40:
            action = "WATCH"

        else:
            action = "NO TRADE"

        if action in ["BUY", "STRONG BUY"]:

            entry = round(df["close"].iloc[-1], 2)

            stoploss = round(entry * 0.99, 2)

            target1 = round(entry * 1.02, 2)

            target2 = round(entry * 1.04, 2)

        else:

            entry = None
            stoploss = None
            target1 = None
            target2 = None

        return {

            "symbol": symbol,

            "action": action,

            "confidence": confidence,

            "score": score,

            "entry": entry,

            "stoploss": stoploss,

            "target1": target1,

            "target2": target2,

            "reasons": result["reasons"]

        }
