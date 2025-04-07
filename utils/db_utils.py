import sqlite3
from typing import List, Dict

class DatabaseManager:
    def __init__(self, db_path: str = "trades.db"):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def init_db(self):
        """Initialize the database with required tables"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            side TEXT NOT NULL,
            entry_price REAL NOT NULL,
            exit_price REAL,
            quantity REAL NOT NULL,
            entry_time TIMESTAMP NOT NULL,
            exit_time TIMESTAMP,
            profit_loss REAL,
            profit_loss_percent REAL,
            status TEXT NOT NULL,
            exit_reason TEXT
        )
        ''')
        
        conn.commit()
        conn.close()

    def fetch_historical_trades(self, limit: int = 100) -> List[Dict]:
        """Fetch historical trades from database"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT id, entry_time, exit_time, symbol, side, entry_price, exit_price, profit_loss,
               exit_reason, quantity, leverage
        FROM trades 
        WHERE status = 'CLOSED' 
        ORDER BY exit_time DESC 
        LIMIT ?
        ''', (limit,))
        
        columns = [description[0] for description in cursor.description]
        trades = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return trades

    def fetch_active_trades(self) -> List[Dict]:
        """Fetch currently active trades"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT id, entry_time, symbol, side, entry_price, quantity, leverage
        FROM trades 
        WHERE status = 'OPEN' 
        ORDER BY entry_time DESC
        ''')
        
        columns = [description[0] for description in cursor.description]
        trades = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return trades

    def get_trading_stats(self) -> Dict:
        """Get overall trading statistics"""
        conn = self._get_connection()
        cursor = conn.cursor()
        
        cursor.execute('''
        SELECT 
            COUNT(*) as total_trades,
            SUM(CASE WHEN profit_loss > 0 THEN 1 ELSE 0 END) as winning_trades,
            SUM(profit_loss) as total_profit_loss,
            AVG(profit_loss_percent) as avg_profit_loss_percent
        FROM trades 
        WHERE status = 'CLOSED'
        ''')
        
        stats = dict(zip(['total_trades', 'winning_trades', 'total_profit_loss', 'avg_profit_loss_percent'], 
                        cursor.fetchone()))
        
        conn.close()
        return stats
    
    def get_unique_symbols(self):
        """Fetch unique symbols from the trades table."""
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT symbol FROM trades")
        symbols = [row[0] for row in cursor.fetchall()]
        conn.close()
        return symbols

    def fetch_filtered_trades(self, symbol=None, start_date=None, end_date=None, profitability=None):
        """Fetch trades with optional filters."""
        conn = self._get_connection()
        cursor = conn.cursor()

        query = """
        SELECT id, timestamp, symbol, side, entry_time, exit_time, entry_price, exit_price, profit_loss,
               trade_duration, initial_sl, final_sl, exit_reason, quantity, leverage
        FROM trades
        WHERE 1=1
        """
        params = []

        if symbol:
            query += " AND symbol = ?"
            params.append(symbol)
        if start_date:
            query += " AND DATE(timestamp) >= ?"
            params.append(start_date)
        if end_date:
            query += " AND DATE(timestamp) <= ?"
            params.append(end_date)
        if profitability == "profitable":
            query += " AND profit_loss > 0"
        elif profitability == "losing":
            query += " AND profit_loss <= 0"

        query += " ORDER BY id DESC"
        cursor.execute(query, params)
        columns = [description[0] for description in cursor.description]
        trades = [dict(zip(columns, row)) for row in cursor.fetchall()]
        conn.close()
        return trades