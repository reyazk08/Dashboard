document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch real-time data
    function fetchRealTimeData() {
        fetch('/api/realtime-data')
            .then(response => response.json())
            .then(data => {
                // Update the dashboard with real-time data
                document.getElementById('realtime-data').innerText = JSON.stringify(data);
            })
            .catch(error => console.error('Error fetching real-time data:', error));
    }

    // Function to fetch historical data
    function fetchHistoricalData() {
        fetch('/api/historical-data')
            .then(response => response.json())
            .then(data => {
                // Update the historical analysis section
                document.getElementById('historical-data').innerText = JSON.stringify(data);
            })
            .catch(error => console.error('Error fetching historical data:', error));
    }

    // Function to control the trading bot
    function controlBot(action) {
        fetch('/api/control-bot', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ action: action })
        })
        .then(response => response.json())
        .then(data => {
            // Update the control section with the response
            document.getElementById('bot-control-response').innerText = data.message;
        })
        .catch(error => console.error('Error controlling bot:', error));
    }

    // Event listeners for bot control buttons
    document.getElementById('start-bot').addEventListener('click', function() {
        controlBot('start');
    });

    document.getElementById('stop-bot').addEventListener('click', function() {
        controlBot('stop');
    });

    // Initial data fetch
    fetchRealTimeData();
    fetchHistoricalData();

    // Set interval for real-time data updates
    setInterval(fetchRealTimeData, 5000); // Update every 5 seconds
});