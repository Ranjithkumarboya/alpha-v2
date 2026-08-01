"""
==================================================
ALPHA v2
Scanner Engine
==================================================
"""

from logger import info


class ScannerEngine:

    def __init__(self):

        info("Scanner Engine Loaded")

        self.watchlist = [
            "RELIANCE",
            "TCS",
            "HDFCBANK",
            "ICICIBANK",
            "SBIN",
            "INFY",
            "LT",
            "AXISBANK",
            "BAJFINANCE",
            "KOTAKBANK"
        ]

    def scan(self):

        results = []

        for stock in self.watchlist:

            results.append({

                "symbol": stock,

                "score": 0,

                "trend": "Unknown",

                "decision": "WAIT"

            })

        return results


scanner = ScannerEngine()
