"""
====================================================
ALPHA v2
Core Engine
====================================================
"""

from utils import market_status
from logger import info


class AlphaEngine:

    def __init__(self):
        info("Alpha Engine Initialized")

    def get_market_status(self):
        return market_status()

    def run(self):

        status = self.get_market_status()

        return {
            "market_status": status,
            "scanner": "Not Started",
            "evidence": "Not Started",
            "portfolio": "Not Started",
            "news": "Not Started",
            "options": "Not Started",
            "decision": "WAIT"
        }


engine = AlphaEngine()
