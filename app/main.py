from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    # Sample data for trading positions
    positions = [
        {"symbol": "BTC/USD", "size": 0.5, "entry_price": 45000, "current_price": 46000, "pnl": "+500"},
        {"symbol": "ETH/USD", "size": 1.0, "entry_price": 3000, "current_price": 3100, "pnl": "+100"},
        {"symbol": "XRP/USD", "size": 2000, "entry_price": 0.5, "current_price": 0.6, "pnl": "+200"},
    ]
    return render_template('dashboard.html', positions=positions)

@app.route('/api/positions')
def get_positions():
    # Simulated real-time data for trading positions
    positions = [
        {"symbol": "BTC/USD", "size": 0.5, "entry_price": 45000, "current_price": 46200, "pnl": "+600"},
        {"symbol": "ETH/USD", "size": 1.0, "entry_price": 3000, "current_price": 3120, "pnl": "+120"},
        {"symbol": "XRP/USD", "size": 2000, "entry_price": 0.5, "current_price": 0.65, "pnl": "+300"},
    ]
    return jsonify(positions)
@app.route('/historical')
def historical():
    return render_template('historical.html')

if __name__ == '__main__':
    app.run(debug=True)