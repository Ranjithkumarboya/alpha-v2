"""
=========================================
ALPHA v2
Professional AI Engine
=========================================
"""

from scanner import Scanner


class AIEngine:

    def __init__(self):

        self.scanner = Scanner()

    def refresh(self):

        self.scanner = Scanner()

    def decision(self):

        self.refresh()

        df = self.scanner.scan()

        if df.empty:

            return {
                "action": "WAIT",
                "confidence": 0,
                "trend": "UNKNOWN",
                "risk": "HIGH"
            }

        if "Signal" not in df.columns:

            return {
                "action": "WAIT",
                "confidence": 0,
                "trend": "UNKNOWN",
                "risk": "HIGH"
            }

        signal = df.iloc[0]["Signal"]

        confidence = df.iloc[0].get("Confidence", 50)

        if signal == "BUY CE":

            return {
                "action": "BUY CALL",
                "confidence": confidence,
                "trend": "Bullish",
                "risk": "Medium"
            }

        elif signal == "BUY PE":

            return {
                "action": "BUY PUT",
                "confidence": confidence,
                "trend": "Bearish",
                "risk": "Medium"
            }

        return {
            "action": "WAIT",
            "confidence": confidence,
            "trend": "Sideways",
            "risk": "Low"
        }

    def summary(self):

        data = self.decision()

        return {

            "Action": data["action"],

            "Confidence": data["confidence"],

            "Trend": data["trend"],

            "Risk": data["risk"]

        }


ai = AIEngine()
