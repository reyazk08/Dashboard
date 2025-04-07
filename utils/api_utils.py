import requests
import re

RASPBERRY_PI_IP = "192.168.1.9"  # Replace with the actual IP address of your Raspberry Pi

def fetch_historical_trades():
    """Fetch historical trades from the Raspberry Pi API."""
    try:
        response = requests.get(f"http://{RASPBERRY_PI_IP}:5000/api/historical-trades")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching historical trades: {e}")
        return []

def fetch_active_trades():
    """Fetch active trades from the Raspberry Pi API."""
    try:
        response = requests.get(f"http://{RASPBERRY_PI_IP}:5000/api/active-trades")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching active trades: {e}")
        return []

def fetch_logs():
    """Fetch and parse logs from the trading_bot.log file."""
    try:
        logs = []
        with open('/path/to/trading_bot.log', 'r') as log_file:
            content = log_file.readlines()

        # Extract the latest HA data for each symbol
        symbol_data = {}
        current_symbol = None
        for line in content:
            # Detect the start of a new symbol's data
            match = re.match(r"--- Latest HA Data \((.*?)\) ---", line)
            if match:
                current_symbol = match.group(1)
                symbol_data[current_symbol] = []
                continue

            # If inside a symbol's section, collect the data
            if current_symbol and line.strip():
                symbol_data[current_symbol].append(line.strip())

        # Format the extracted data for display
        for symbol, data in symbol_data.items():
            logs.append(f"Symbol: {symbol}")
            logs.extend(data)

        # Add the last 10 general log entries
        logs.append("\n--- General Logs ---")
        logs.extend(content[-10:])

        return logs
    except Exception as e:
        print(f"Error fetching logs: {e}")
        return ["Error fetching logs."]

def fetch_bot_status():
    """Fetch the bot's status from the Raspberry Pi API."""
    try:
        response = requests.get(f"http://{RASPBERRY_PI_IP}:5000/api/status")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching bot status: {e}")
        return {"status": "Unknown", "timeframe": "N/A"}