
"""
====================================================
ALPHA v2.0
Utility Functions
====================================================
"""

from datetime import datetime, time
from zoneinfo import ZoneInfo

IST = ZoneInfo("Asia/Kolkata")


def now():
    """Current IST datetime"""
    return datetime.now(IST)


def today():
    return now().date()


def current_time():
    return now().time()


def market_status():

    t = current_time()

    if t < time(9, 15):
        return "PRE MARKET"

    elif t <= time(15, 30):
        return "MARKET OPEN"

    return "MARKET CLOSED"


def is_market_open():

    return market_status() == "MARKET OPEN"


def format_currency(value):

    return f"₹{value:,.2f}"


def format_percent(value):

    return f"{value:.2f}%"


def score_color(score):

    if score >= 80:
        return "green"

    elif score >= 70:
        return "orange"

    return "red"


def recommendation(score):

    if score >= 80:
        return "STRONG BUY"

    elif score >= 70:
        return "BUY"

    elif score >= 60:
        return "WATCH"

    return "NO TRADE"


def safe_float(value, default=0.0):

    try:
        return float(value)
    except Exception:
        return default


def safe_int(value, default=0):

    try:
        return int(value)
    except Exception:
        return default
