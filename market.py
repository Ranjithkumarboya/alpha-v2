"""
=========================================
ALPHA v2
Professional Market Engine
=========================================
"""

from datetime import datetime, time, timedelta


class MarketEngine:

    def __init__(self):
        pass

    def market_status(self):

        now = datetime.now()

        # Saturday / Sunday
        if now.weekday() >= 5:
            return "MARKET CLOSED"

        current = now.time()

        if current < time(9, 0):
            return "MARKET CLOSED"

        elif current < time(9, 15):
            return "PRE MARKET"

        elif current <= time(15, 30):
            return "MARKET OPEN"

        return "MARKET CLOSED"

    def market_regime(self):

        # AI Engine will replace this later
        return "UNKNOWN"

    def current_expiry(self):

        today = datetime.today()

        days = (3 - today.weekday()) % 7

        expiry = today + timedelta(days=days)

        return expiry.strftime("%d %b %Y")

    def is_expiry_day(self):

        today = datetime.today()

        if today.weekday() != 3:
            return False

        return True

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
