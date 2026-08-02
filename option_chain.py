from datetime import datetime
from market_data import MarketData


class OptionChain:

    def __init__(self):
        self.market = MarketData()

    def atm_strike(self):
        nifty = self.market.ltp("NSE:NIFTY 50")

        if nifty is None:
            return None

        return round(nifty / 50) * 50

    def current_expiry(self):
        today = datetime.today()

        year = str(today.year)[2:]
        month = today.strftime("%b").upper()

        return f"{year}{month}"

    def option_symbols(self):

        strike = self.atm_strike()

        if strike is None:
            return None

        expiry = self.current_expiry()

        ce = f"NFO:NIFTY{expiry}{strike}CE"
        pe = f"NFO:NIFTY{expiry}{strike}PE"

        return {
            "CE": ce,
            "PE": pe
        }

    def option_prices(self):

        symbols = self.option_symbols()

        if symbols is None:
            return {
                "CE": None,
                "PE": None
            }

        ce = self.market.ltp(symbols["CE"])
        pe = self.market.ltp(symbols["PE"])

        return {
            "CE": ce,
            "PE": pe
        }
