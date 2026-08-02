"""
=========================================
ALPHA v2
Professional AI Engine
=========================================
"""

from scanner import scanner


class AIEngine:

    def decision(self):

        df = scanner.scan()

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

        if signal == "BUY CE":
            return {
                "action": "BUY CALL",
                "confidence": 75,
                "trend": "Bullish",
                "risk": "Medium"
            }

        if signal == "BUY PE":
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

        data = self.decision()

        return {
            "Action": data["action"],
            "Confidence": data["confidence"],
            "Trend": data["trend"],
            "Risk": data["risk"]
        }


ai = AIEngine()
