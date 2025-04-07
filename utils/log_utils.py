import os

def fetch_logs():
    if not os.path.exists('trading_bot.log'):
        return []

    with open('trading_bot.log', 'r') as f:
        logs = f.readlines()
    
    return logs[-100:]  # Return the last 100 log entries

def filter_logs(keyword):
    if not os.path.exists('trading_bot.log'):
        return []

    with open('trading_bot.log', 'r') as f:
        logs = f.readlines()
    
    filtered_logs = [log for log in logs if keyword in log]
    return filtered_logs

def highlight_errors(logs):
    highlighted_logs = []
    for log in logs:
        if 'ERROR' in log:
            highlighted_logs.append(f"<span style='color:red;'>{log}</span>")
        elif 'WARNING' in log:
            highlighted_logs.append(f"<span style='color:orange;'>{log}</span>")
        else:
            highlighted_logs.append(log)
    return highlighted_logs