"""
=========================================
ALPHA v2
Professional Option Chain Engine
=========================================
"""

from datetime import datetime

from market_data import MarketData


class OptionChain:

    def __init__(self):

        self.market = MarketData()

    def spot_price(self):

        return self.market.ltp("NSE:NIFTY 50")

    def atm_strike(self):

        spot = self.spot_price()

        if spot is None:
            return None

        return round(spot / 50) * 50

    def expiry_code(self):

        today = datetime.today()

        year = str(today.year)[2:]

        month = today.strftime("%b").upper()

        return f"{year}{month}"

    def option_symbols(self):

        strike = self.atm_strike()

        expiry = self.expiry_code()

        ce = f"NFO:NIFTY{expiry}{strike}CE"
        pe = f"NFO:NIFTY{expiry}{strike}PE"

        return {
            "CE": ce,
            "PE": pe
        }

    def option_prices(self):

        symbols = self.option_symbols()

        ce = self.market.ltp(symbols["CE"])
        pe = self.market.ltp(symbols["PE"])

        return {
            "CE": ce,
            "PE": pe
        }

    def summary(self):

        strike = self.atm_strike()

        symbols = self.option_symbols()

        prices = self.option_prices()

        return {

            "spot": self.spot_price(),

            "strike": strike,

            "ce_symbol": symbols["CE"],

            "pe_symbol": symbols["PE"],

            "ce_price": prices["CE"],

            "pe_price": prices["PE"]

        }


option_chain = OptionChain()
