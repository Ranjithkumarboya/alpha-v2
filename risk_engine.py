"""
====================================================
ALPHA v2
Risk Engine
====================================================
"""

from logger import info


class RiskEngine:

    def __init__(self):
        info("Risk Engine Loaded")

    def position_size(
        self,
        capital,
        risk_percent,
        entry,
        stoploss
    ):

        risk_amount = capital * (risk_percent / 100)

        difference = abs(entry - stoploss)

        if difference == 0:
            quantity = 0
        else:
            quantity = int(risk_amount / difference)

        return {
            "capital": capital,
            "risk_amount": round(risk_amount, 2),
            "quantity": quantity
        }

    def risk_level(self, rr):

        if rr >= 3:
            return "LOW"

        elif rr >= 2:
            return "MEDIUM"

        return "HIGH"


risk = RiskEngine()
