"""
====================================================
ALPHA v2
Professional Market Engine
====================================================
"""

from datetime import datetime, time, timedelta

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
        AI Engine will replace this with
        Bullish / Bearish / Sideways.
        """
        return "UNKNOWN"

    def current_expiry(self):

        today = datetime.today()

        days = (3 - today.weekday()) % 7

        expiry = today + timedelta(days=days)

        return expiry.strftime("%d %b %Y")

    def is_expiry_day(self):

        return datetime.today().weekday() == 3

    def market_open(self):

        return self.market_status() == "MARKET OPEN"

    def summary(self):

        return {

            "status": self.market_status(),

            "regime": self.market_regime(),

            "expiry": self.current_expiry(),

            "is_expiry": self.is_expiry_day(),

            "market_open": self.market_open()

        }


market = MarketEngine()
