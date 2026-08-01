"""
====================================================
ALPHA v2
Market Engine
====================================================
"""

from datetime import datetime, time

from logger import info


class MarketEngine:

    def __init__(self):
        info("Market Engine Loaded")

    def market_status(self):

        now = datetime.now().time()

        if now < time(9, 15):
            return "PRE MARKET"

        elif now <= time(15, 30):
            return "MARKET OPEN"

        return "MARKET CLOSED"

    def market_regime(self):
        """
        Placeholder.
        Will be upgraded with live NIFTY and INDIA VIX.
        """
        return "UNKNOWN"

    def is_expiry_day(self):

        today = datetime.now()

        # Thursday = 3
        return today.weekday() == 3

    def summary(self):

        return {

            "status": self.market_status(),

            "regime": self.market_regime(),

            "expiry": self.is_expiry_day()

        }


market = MarketEngine()
