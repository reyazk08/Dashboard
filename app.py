from flask import Flask, render_template, jsonify, make_response, request
from datetime import datetime
from utils.api_utils import fetch_bot_status, fetch_active_trades, fetch_historical_trades, fetch_logs
from utils.db_utils import DatabaseManager

db_manager = DatabaseManager("trades.db")
app = Flask(__name__)

@app.route('/active-trades', methods=['GET'])
def active_trades():
    """Active trades page."""
    try:
        # Fetch active trades from the database
        trades = db_manager.fetch_active_trades()

        # Calculate summary stats
        total_pnl = sum(trade['pnl'] for trade in trades if trade.get('pnl'))
        total_positions = len(trades)
        winning_positions = sum(1 for trade in trades if trade.get('pnl') and trade['pnl'] > 0)
        losing_positions = sum(1 for trade in trades if trade.get('pnl') and trade['pnl'] <= 0)
    except Exception as e:
        print(f"Error fetching active trades: {e}")
        trades = []
        total_pnl = 0
        total_positions = 0
        winning_positions = 0
        losing_positions = 0

    return render_template(
        'active_trades.html',
        trades=trades,
        total_pnl=total_pnl,
        total_positions=total_positions,
        winning_positions=winning_positions,
        losing_positions=losing_positions
    )

@app.route('/logs')
def logs():
    try:
        # Fetch logs from the Raspberry Pi API
        response = requests.get(f"http://{RASPBERRY_PI_IP}:5000/api/logs")
        response.raise_for_status()
        logs = response.json()
    except Exception as e:
        print(f"Error fetching logs: {e}")
        logs = ["Error fetching logs."]
    
    # Debug: Print logs to verify
    print(logs)

    # Render the logs.html template with the fetched logs
    return render_template('logs.html', logs=logs)

@app.route('/trades', methods=['GET'])
def trades():
    # Get filter parameters from the request
    symbol = request.args.get('symbol')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    profitability = request.args.get('profitability')

    try:
        # Fetch historical trades from the Raspberry Pi API
        historical_trades = fetch_historical_trades()

        # Apply filters
        if symbol:
            historical_trades = [trade for trade in historical_trades if trade['symbol'] == symbol]
        if start_date:
            start_timestamp = int(datetime.strptime(start_date, "%Y-%m-%d").timestamp())
            historical_trades = [trade for trade in historical_trades if trade['entry_time'] >= start_timestamp]
        if end_date:
            end_timestamp = int(datetime.strptime(end_date, "%Y-%m-%d").timestamp())
            historical_trades = [trade for trade in historical_trades if trade['exit_time'] <= end_timestamp]
        if profitability == "profitable":
            historical_trades = [trade for trade in historical_trades if trade['profit_loss'] > 0]
        elif profitability == "losing":
            historical_trades = [trade for trade in historical_trades if trade['profit_loss'] <= 0]

    except Exception as e:
        print(f"Error fetching historical trades: {e}")
        historical_trades = []

    # Render the trades.html template with the filtered trades
    return render_template('trades.html', trades=historical_trades)

@app.route('/export-trades')
def export_trades():
    try:
        # Fetch historical trades from the Raspberry Pi API
        historical_trades = fetch_historical_trades()

        # Generate CSV data
        csv_data = "id,symbol,side,entry_price,exit_price,profit_loss,trade_duration,exit_reason,quantity,leverage\n"
        for trade in historical_trades:
            csv_data += f"{trade['id']},{trade['symbol']},{trade['side']},{trade['entry_price']},{trade['exit_price']},{trade['profit_loss']},{trade['trade_duration']},{trade['exit_reason']},{trade['quantity']},{trade['leverage']}\n"

        # Create a response with the CSV data
        response = make_response(csv_data)
        response.headers["Content-Disposition"] = "attachment; filename=historical_trades.csv"
        response.headers["Content-Type"] = "text/csv"
        return response

    except Exception as e:
        print(f"Error exporting trades: {e}")
        return "Error exporting trades", 500

@app.route('/')
def index():
    try:
        # Fetch active trades from the Raspberry Pi API
        active_trades = fetch_active_trades()
    except Exception as e:
        print(f"Error fetching active trades: {e}")
        active_trades = []

    try:
        # Fetch bot status from the Raspberry Pi API
        bot_status = fetch_bot_status()
    except Exception as e:
        print(f"Error fetching bot status: {e}")
        bot_status = {"status": "Unknown", "timeframe": "N/A"}

    try:
        # Fetch logs from the Raspberry Pi API
        error_logs = fetch_logs()[:5]  # Show only the first 5 logs as highlights
    except Exception as e:
        print(f"Error fetching logs: {e}")
        error_logs = ["Error fetching logs."]

    # Dummy performance data for the chart
    performance_data = {
        "labels": ["Jan", "Feb", "Mar", "Apr", "May"],
        "profits": [500, 700, 800, 600, 900],
        "losses": [200, 300, 100, 400, 150]
    }

    try:
        # Fetch historical trades for analytics
        historical_trades = fetch_historical_trades()
        total_trades = len(historical_trades)
        avg_trade_duration = sum(trade['trade_duration'] for trade in historical_trades) / total_trades if total_trades > 0 else 0
        best_trade = max(historical_trades, key=lambda x: x['profit_loss'], default=None)
        worst_trade = min(historical_trades, key=lambda x: x['profit_loss'], default=None)
    except Exception as e:
        print(f"Error fetching historical trades: {e}")
        total_trades = 0
        avg_trade_duration = 0
        best_trade = None
        worst_trade = None

    # Render the index.html template with the data
    return render_template(
        'index.html',
        total_trades=total_trades,
        avg_trade_duration=avg_trade_duration,
        best_trade=best_trade,
        worst_trade=worst_trade,
        active_trades=active_trades,
        bot_status=bot_status,
        error_logs=error_logs,
        performance_data=performance_data
    )

if __name__ == "__main__":
    app.run(debug=True)