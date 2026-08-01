"""
====================================================
ALPHA v2
Evidence Engine
====================================================
"""

from logger import info


class EvidenceEngine:

    def __init__(self):
        info("Evidence Engine Loaded")

    def analyse(self, symbol):

        return {

            "symbol": symbol,

            "historical_trades": 0,

            "wins": 0,

            "losses": 0,

            "win_rate": 0,

            "expectancy": 0,

            "profit_factor": 0,

            "max_drawdown": 0,

            "status": "NO DATA"

        }

    def recommendation(self, symbol):

        data = self.analyse(symbol)

        if data["win_rate"] >= 60:
            decision = "PASS"
        else:
            decision = "FAIL"

        data["decision"] = decision

        return data


evidence = EvidenceEngine()
