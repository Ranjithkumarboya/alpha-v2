"""
===========================================================
ALPHA v2.0.0
Global Configuration
===========================================================
"""

from pathlib import Path
from datetime import time

# =========================================================
# APPLICATION
# =========================================================

APP_NAME = "ALPHA"
APP_VERSION = "2.0.0"
APP_BUILD = "Foundation"
APP_AUTHOR = "Ranjith & ChatGPT"

# =========================================================
# PATHS
# =========================================================

ROOT_DIR = Path(__file__).parent

DATA_DIR = ROOT_DIR / "data"
LOG_DIR = ROOT_DIR / "logs"

DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

TRADES_DB = DATA_DIR / "trades.db"
DATABASE_FILE = TRADES_DB
EVIDENCE_DB = DATA_DIR / "evidence.db"

LOG_FILE = LOG_DIR / "alpha.log"

# =========================================================
# DEFAULT TRADING SETTINGS
# =========================================================

DEFAULT_CAPITAL = 100000

DEFAULT_RISK_PERCENT = 1.0

MAX_OPEN_TRADES = 3

MIN_SCORE = 70

WATCHLIST_SIZE = 30

# =========================================================
# MARKET TIMINGS
# =========================================================

PRE_MARKET_START = time(9, 0)

MARKET_OPEN = time(9, 15)

MARKET_CLOSE = time(15, 30)

POST_MARKET_END = time(16, 0)

# =========================================================
# REFRESH SETTINGS
# =========================================================

LIVE_REFRESH_SECONDS = 30

AUTO_REFRESH = True

# =========================================================
# FEATURE FLAGS
# =========================================================

ENABLE_SCANNER = True

ENABLE_OPTIONS = True

ENABLE_EVIDENCE_ENGINE = True

ENABLE_NEWS_ENGINE = True

ENABLE_PORTFOLIO = True

ENABLE_DIAGNOSTICS = True

ENABLE_LOGGING = True

# =========================================================
# OPTION SETTINGS
# =========================================================

ALLOW_OPTION_BUYING = True

ALLOW_OPTION_SELLING = False

DEFAULT_TARGET_RR = 2.0

MAX_SPREAD_PERCENT = 1.5

# =========================================================
# NEWS SETTINGS
# =========================================================

NEWS_LOOKBACK_HOURS = 24

MAX_NEWS_PER_STOCK = 5

# =========================================================
# UI SETTINGS
# =========================================================

PAGE_TITLE = "ALPHA v2"

PAGE_ICON = "📈"

LAYOUT = "wide"

# =========================================================
# LOGGING
# =========================================================

LOG_LEVEL = "INFO"

# =========================================================
# ZERODHA
# =========================================================

API_KEY = ""

API_SECRET = ""

REDIRECT_URL = ""

# =========================================================
# END
# =========================================================
