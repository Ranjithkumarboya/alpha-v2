"""
=========================================
ALPHA v2
Professional AI Engine
=========================================
"""

from scanner import scanner


class AIEngine:

    def __init__(self):
        pass

    def decision(self):

        df = scanner.scan()

        row = df.iloc[0]

        signal = row["Signal"]

        if signal == "BUY CE":

            return {
                "action": "BUY CALL",
                "confidence": 75,
                "trend": "Bullish",
                "risk": "Medium"
            }

        elif signal == "BUY PE":

            return {
                "action": "BUY PUT",
                "confidence": 75,
                "trend": "Bearish",
                "risk": "Medium"
            }

        return {
            "action": "WAIT",
            "confidence": 50,
            "trend": "Sideways",
            "risk": "Low"
        }

    def summary(self):

        ai = self.decision()

        return {

            "Action": ai["action"],

            "Confidence": ai["confidence"],

            "Trend": ai["trend"],

            "Risk": ai["risk"]

        }


ai = AIEngine()
