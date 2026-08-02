"""
=========================================
ALPHA v2
Professional Option Chain Engine
=========================================
"""

from market_data import MarketData


class OptionChain:

    def __init__(self):

        self.market = MarketData()

    def spot(self):

        return self.market.ltp("NSE:NIFTY 50")

    def atm_strike(self):

        spot = self.spot()

        if spot is None:
            return None

        return round(spot / 50) * 50

    def option_chain(self):

        df = self.market.nifty_option_chain()

        if df.empty:
            return None

        expiry = sorted(df["expiry"].unique())[0]

        df = df[df["expiry"] == expiry]

        return df.reset_index(drop=True)

    def atm_options(self):

        df = self.option_chain()

        if df is None:
            return None

        strike = self.atm_strike()

        atm = df[df["strike"] == strike]

        if atm.empty:
            return None

        ce = atm[df["instrument_type"] == "CE"].iloc[0]
        pe = atm[df["instrument_type"] == "PE"].iloc[0]

        return {

            "strike": strike,

            "ce_symbol": ce["tradingsymbol"],

            "pe_symbol": pe["tradingsymbol"]

        }

    def option_prices(self):

        option = self.atm_options()

        if option is None:
            return None

        ce_price = self.market.ltp(
            "NFO:" + option["ce_symbol"]
        )

        pe_price = self.market.ltp(
            "NFO:" + option["pe_symbol"]
        )

        return {

            "spot": self.spot(),

            "strike": option["strike"],

            "ce_symbol": option["ce_symbol"],

            "pe_symbol": option["pe_symbol"],

            "ce_price": ce_price,

            "pe_price": pe_price

        }

    def summary(self):

        return self.option_prices()


option_chain = OptionChain()
