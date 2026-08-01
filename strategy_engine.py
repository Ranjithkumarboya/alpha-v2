"""
====================================================
ALPHA v2
Strategy Engine
====================================================
"""

from logger import info


class StrategyEngine:

    def __init__(self):

        info("Strategy Engine Loaded")

    def trend_following(self, stock):

        return {
            "strategy": "Trend Following",
            "score": 0,
            "status": "Pending"
        }

    def breakout(self, stock):

        return {
            "strategy": "Breakout",
            "score": 0,
            "status": "Pending"
        }

    def pullback(self, stock):

        return {
            "strategy": "Pullback",
            "score": 0,
            "status": "Pending"
        }

    def option_buying(self, stock):

        return {
            "strategy": "Option Buying",
            "score": 0,
            "status": "Pending"
        }

    def evaluate(self, stock):

        return [

            self.trend_following(stock),

            self.breakout(stock),

            self.pullback(stock),

            self.option_buying(stock)

        ]


strategy = StrategyEngine()
