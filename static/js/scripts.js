// This file contains optional JavaScript for interactivity, such as auto-refreshing the homepage every 30 seconds.

function refreshData() {
    fetch('/')
        .then(response => response.text())
        .then(data => {
            document.open();
            document.write(data);
            document.close();
        })
        .catch(error => console.error('Error fetching data:', error));
}

// Set interval to refresh the homepage every 30 seconds
setInterval(refreshData, 30000);