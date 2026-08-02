"""
=========================================
ALPHA v2
Professional Scanner Engine
=========================================
"""

import pandas as pd

from option_chain import option_chain
from market_data import MarketData


class Scanner:

    def __init__(self):

        self.market = MarketData()

    def scan(self):

        option = option_chain.summary()

        spot = option["spot"]
        strike = option["strike"]

        ce = option["ce_price"]
        pe = option["pe_price"]

        signal = "WAIT"

        if ce is not None and pe is not None:

            if ce > pe:
                signal = "BUY CE"

            elif pe > ce:
                signal = "BUY PE"

        data = [

            {
                "Spot": spot,
                "ATM": strike,
                "CE Premium": ce,
                "PE Premium": pe,
                "Signal": signal
            }

        ]

        return pd.DataFrame(data)


scanner = Scanner()
