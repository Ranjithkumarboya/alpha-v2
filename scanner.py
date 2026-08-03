"""
=========================================
ALPHA v2
Professional Scanner Engine
=========================================
"""

import pandas as pd

from option_chain import OptionChain


class Scanner:

    def __init__(self):

        self.option_chain = OptionChain()

    def refresh(self):

        self.option_chain = OptionChain()

    def scan(self):

        self.refresh()

        option = self.option_chain.summary()

        if option is None:

            return pd.DataFrame([
                {
                    "Status": "Market data unavailable"
                }
            ])

        ce = option.get("ce_price")
        pe = option.get("pe_price")

        signal = "WAIT"

        confidence = 50

        if ce is not None and pe is not None:

            if ce > pe:

                signal = "BUY CE"
                confidence = 75

            elif pe > ce:

                signal = "BUY PE"
                confidence = 75

        return pd.DataFrame([
            {
                "ATM": option["strike"],
                "Spot": option["spot"],
                "CE Premium": ce,
                "PE Premium": pe,
                "Signal": signal,
                "Confidence": confidence
            }
        ])


scanner = Scanner()
