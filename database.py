"""
====================================================
ALPHA v2.0
Database Manager
====================================================
"""

import sqlite3
from pathlib import Path

from config import DATABASE_FILE


class DatabaseManager:

    def __init__(self):
        self.db = DATABASE_FILE
        self.create_database()

    def connect(self):
        return sqlite3.connect(self.db)

    def create_database(self):

        conn = self.connect()
        cur = conn.cursor()

        # ==========================================
        # Trade Journal
        # ==========================================

        cur.execute("""
        CREATE TABLE IF NOT EXISTS trades(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            strategy TEXT,

            direction TEXT,

            entry REAL,

            stoploss REAL,

            target REAL,

            quantity INTEGER,

            status TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        # ==========================================
        # Scanner History
        # ==========================================

        cur.execute("""
        CREATE TABLE IF NOT EXISTS scanner_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            score REAL,

            strategy TEXT,

            recommendation TEXT,

            market_regime TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        # ==========================================
        # Historical Evidence
        # ==========================================

        cur.execute("""
        CREATE TABLE IF NOT EXISTS evidence(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            strategy TEXT,

            trades INTEGER,

            winrate REAL,

            expectancy REAL,

            profit_factor REAL,

            drawdown REAL,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        # ==========================================
        # Portfolio
        # ==========================================

        cur.execute("""
        CREATE TABLE IF NOT EXISTS portfolio(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            quantity INTEGER,

            average_price REAL,

            current_price REAL,

            pnl REAL,

            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """)

        conn.commit()
        conn.close()


db = DatabaseManager()
