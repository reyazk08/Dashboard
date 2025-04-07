# Dashboard for Trading Bot

This project is a Flask-based dashboard designed to monitor and display the status of a trading bot running on a Raspberry Pi. The dashboard fetches data from the bot's SQLite database and log files, providing real-time insights into the bot's performance and activity.

## Project Structure

```
dashboard/
├── app.py                 # Main Flask app
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   │   └── styles.css     # Custom styles for the dashboard
│   └── js/
│       └── scripts.js     # Optional JavaScript for interactivity
├── templates/             # HTML templates for the dashboard
│   ├── base.html          # Base layout for all pages
│   ├── index.html         # Homepage (Bot status and summary)
│   ├── trades.html        # Historical trades page
│   ├── active_trades.html # Active trades page
│   └── logs.html          # Logs page
├── utils/                 # Utility functions
│   ├── db_utils.py        # Functions to interact with SQLite database
│   ├── log_utils.py       # Functions to parse and display logs
│   └── api_utils.py       # Functions to fetch data from the bot's API
└── requirements.txt       # Python dependencies
```

## Features

- **Real-time Bot Status**: The homepage displays the bot's current status, including uptime, balance, and active trades.
- **Active Trades Monitoring**: A dedicated page shows details of currently active trades, including entry price, current price, and unrealized P&L.
- **Historical Trade Records**: View a comprehensive history of completed trades with filtering options for date range and profitability.
- **Log Viewer**: Access and search through the bot's logs for debugging and monitoring purposes.

## Setup Instructions

1. **Clone the Repository**:
   ```
   git clone <repository-url>
   cd dashboard
   ```

2. **Install Dependencies**:
   Ensure you have Python and pip installed, then run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Dashboard**:
   Start the Flask application:
   ```
   python app.py
   ```

4. **Access the Dashboard**:
   Open your web browser and navigate to `http://localhost:5000` to view the dashboard.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.