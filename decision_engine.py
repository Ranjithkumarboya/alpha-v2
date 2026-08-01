"""
====================================================
ALPHA v2
Decision Engine
====================================================
"""

from logger import info


class DecisionEngine:

    def __init__(self):
        info("Decision Engine Loaded")

    def evaluate(
        self,
        market,
        strategy,
        evidence,
        news,
        risk
    ):

        reasons = []

        score = 0

        # --------------------------
        # Market
        # --------------------------

        if market == "Bullish":
            score += 20
            reasons.append("Bullish Market")

        elif market == "Bearish":
            score -= 20
            reasons.append("Bearish Market")

        # --------------------------
        # Strategy
        # --------------------------

        if strategy == "PASS":
            score += 20
            reasons.append("Strategy Valid")

        # --------------------------
        # Evidence
        # --------------------------

        if evidence == "PASS":
            score += 25
            reasons.append("Historical Edge")

        # --------------------------
        # News
        # --------------------------

        if news == "Positive":
            score += 15
            reasons.append("Positive News")

        elif news == "Negative":
            score -= 20
            reasons.append("Negative News")

        # --------------------------
        # Risk
        # --------------------------

        if risk == "LOW":
            score += 20

        elif risk == "HIGH":
            score -= 20

        # --------------------------
        # Final Decision
        # --------------------------

        if score >= 75:

            decision = "BUY"

        elif score >= 50:

            decision = "WATCH"

        else:

            decision = "NO TRADE"

        return {

            "decision": decision,

            "score": score,

            "reasons": reasons

        }


decision = DecisionEngine()
