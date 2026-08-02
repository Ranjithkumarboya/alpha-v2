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

    def atm_options(self):

        df = self.market.nifty_option_chain()

        if df.empty:
            return None

        strike = self.atm_strike()

        if strike is None:
            return None

        expiry = df["expiry"].min()

        df = df[df["expiry"] == expiry]

        ce = df[
            (df["strike"] == strike) &
            (df["instrument_type"] == "CE")
        ]

        pe = df[
            (df["strike"] == strike) &
            (df["instrument_type"] == "PE")
        ]

        if ce.empty or pe.empty:
            return None

        ce = ce.iloc[0]
        pe = pe.iloc[0]

        return {

            "spot": self.spot(),

            "strike": strike,

            "ce_symbol": ce["tradingsymbol"],

            "pe_symbol": pe["tradingsymbol"]

        }

    def summary(self):

        option = self.atm_options()

        if option is None:
            return None

        ce_price = self.market.ltp(
            "NFO:" + option["ce_symbol"]
        )

        pe_price = self.market.ltp(
            "NFO:" + option["pe_symbol"]
        )

        option["ce_price"] = ce_price
        option["pe_price"] = pe_price

        return option


option_chain = OptionChain()
