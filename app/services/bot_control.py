from flask import current_app

class BotControl:
    def __init__(self):
        self.active_bots = {}
    
    def start_bot(self, bot_id, symbol):
        if bot_id not in self.active_bots:
            self.active_bots[bot_id] = symbol
            # Logic to start the trading bot
            current_app.logger.info(f"Started bot {bot_id} for symbol {symbol}")
            return True
        return False
    
    def stop_bot(self, bot_id):
        if bot_id in self.active_bots:
            del self.active_bots[bot_id]
            # Logic to stop the trading bot
            current_app.logger.info(f"Stopped bot {bot_id}")
            return True
        return False
    
    def emergency_stop(self):
        # Logic to stop all trading bots
        self.active_bots.clear()
        current_app.logger.warning("Emergency stop activated. All bots have been stopped.")
    
    def get_active_bots(self):
        return self.active_bots
    
    def manage_symbol(self, bot_id, new_symbol):
        if bot_id in self.active_bots:
            self.active_bots[bot_id] = new_symbol
            current_app.logger.info(f"Bot {bot_id} symbol changed to {new_symbol}")
            return True
        return False