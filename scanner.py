import pandas as pd

from option_chain import option_chain


class Scanner:

    def scan(self):

        option = option_chain.summary()

        if option is None:

            return pd.DataFrame([
                {
                    "Status": "Market data unavailable"
                }
            ])

        ce = option.get("ce_price")
        pe = option.get("pe_price")

        signal = "WAIT"

        if ce is not None and pe is not None:

            if ce > pe:
                signal = "BUY CE"

            elif pe > ce:
                signal = "BUY PE"

        return pd.DataFrame([
            {
                "ATM": option["strike"],
                "CE Premium": ce,
                "PE Premium": pe,
                "Signal": signal
            }
        ])


scanner = Scanner()
