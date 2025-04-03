from datetime import datetime
import random

class MonitoringService:
    def __init__(self):
        self.positions = []
        self.market_data = []

    def update_market_data(self):
        # Simulate fetching market data
        new_data = {
            'timestamp': datetime.now(),
            'price': random.uniform(100, 200),
            'volume': random.randint(1, 100)
        }
        self.market_data.append(new_data)

    def get_real_time_data(self):
        self.update_market_data()
        return self.market_data[-1] if self.market_data else None

    def add_position(self, symbol, quantity):
        position = {
            'symbol': symbol,
            'quantity': quantity,
            'entry_price': random.uniform(100, 200),
            'timestamp': datetime.now()
        }
        self.positions.append(position)

    def get_positions(self):
        return self.positions

    def get_position_summary(self):
        summary = {}
        for position in self.positions:
            symbol = position['symbol']
            if symbol not in summary:
                summary[symbol] = 0
            summary[symbol] += position['quantity']
        return summary

    def clear_data(self):
        self.positions.clear()
        self.market_data.clear()