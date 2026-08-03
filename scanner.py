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

        spot = option.get("spot")
        strike = option.get("strike")
        ce = option.get("ce_price")
        pe = option.get("pe_price")

        signal = "WAIT"
        trend = "SIDEWAYS"
        confidence = 50

        if ce is not None and pe is not None:

            diff = abs(ce - pe)

            if ce > pe:

                signal = "BUY CE"
                trend = "BULLISH"

            elif pe > ce:

                signal = "BUY PE"
                trend = "BEARISH"

            confidence = min(
                95,
                50 + int(diff / 2)
            )

        return pd.DataFrame([
            {
                "Spot": spot,
                "ATM": strike,
                "CE Premium": ce,
                "PE Premium": pe,
                "Trend": trend,
                "Signal": signal,
                "Confidence": confidence
            }
        ])


scanner = Scanner()
