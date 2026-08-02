from market_data import MarketData


class OptionChain:

    def __init__(self):
        self.market = MarketData()

    def atm_strike(self):
        nifty = self.market.ltp("NSE:NIFTY 50")
        return round(nifty / 50) * 50

    def option_symbols(self):
        strike = self.atm_strike()

        ce = f"NFO:NIFTYAUTO{strike}CE"
        pe = f"NFO:NIFTYAUTO{strike}PE"

        return {
            "CE": ce,
            "PE": pe
        }

    def option_prices(self):
        symbols = self.option_symbols()

        ce_price = self.market.ltp(symbols["CE"])
        pe_price = self.market.ltp(symbols["PE"])

        return {
            "CE": ce_price,
            "PE": pe_price
        }
