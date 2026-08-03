"""
=========================================
ALPHA v2
Professional Market Engine
=========================================
"""

from datetime import datetime, time, timedelta
from market_data import market_data


class MarketEngine:

    def __init__(self):
        pass

    def market_status(self):

        # If we can fetch live market data,
        # the market is open.
        try:
            ltp = market_data.ltp("NSE:NIFTY 50")

            if ltp is not None:
                return "MARKET OPEN"

        except:
            pass

        now = datetime.now()

        # Saturday / Sunday
        if now.weekday() >= 5:
            return "MARKET CLOSED"

        current = now.time()

        if current < time(9, 15):
            return "MARKET CLOSED"

        elif current <= time(15, 30):
            return "MARKET OPEN"

        return "MARKET CLOSED"

    def market_regime(self):

        try:

            quote = market_data.quote("NSE:NIFTY 50")

            if quote is None:
                return "UNKNOWN"

            ohlc = quote["ohlc"]

            last = quote["last_price"]

            open_price = ohlc["open"]

            if last > open_price:
                return "BULLISH"

            elif last < open_price:
                return "BEARISH"

            else:
                return "SIDEWAYS"

        except:
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
