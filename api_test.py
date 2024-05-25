from flask import Flask, jsonify, request
import os
import json
from datetime import datetime, timedelta
import pandas as pd

app = Flask(__name__)
data_directory = "."  # Directory where data files are stored

def load_data(directory="."):
    """
    Load data from JSON files in the specified directory.
    Returns a list of dictionaries containing the data.
    """
    data = []
    for filename in os.listdir(directory):
        if filename.endswith(".json") and filename.startswith("data_"):
            timestamp_str = filename.split("_")[1]  # Extract timestamp from filename
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d_%H-%M-%S")
            with open(os.path.join(directory, filename), 'r') as file:
                file_data = json.load(file)
                for item in file_data:
                    item["timestamp"] = timestamp.strftime("%Y-%m-%d %H:%M:%S")  # Add timestamp to each item
                data.extend(file_data)
    return data

def filter_data(data, start_time=None, end_time=None):
    """
    Filter data based on start and end times with a precision of 1 minute.
    Returns filtered data.
    """
    if start_time is None and end_time is None:
        return data
    filtered_data = []
    for item in data:
        timestamp_str = item.get("timestamp", "")
        if timestamp_str:
            timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            if start_time is not None and timestamp < start_time:
                continue
            if end_time is not None and timestamp > end_time:
                continue
            filtered_data.append(item)
    return filtered_data

@app.route('/api/tabular_data', methods=['GET'])
def get_tabular_data():
    start_date_str = request.args.get('start_date')
    end_date_str = request.args.get('end_date')
    
    # Parse start_date and end_date strings
    start_date, start_time = start_date_str.split("_") if "_" in start_date_str else (start_date_str, "00-00-00")
    end_date, end_time = end_date_str.split("_") if "_" in end_date_str else (end_date_str, "23-59-59")
    
    # Construct start and end times with 1-minute precision
    start_time = datetime.strptime(start_date + "_" + start_time, "%Y-%m-%d_%H-%M-%S")
    end_time = datetime.strptime(end_date + "_" + end_time, "%Y-%m-%d_%H-%M-%S")
    
    # Filter data based on start and end times
    data = load_data(data_directory)
    filtered_data = filter_data(data, start_time, end_time)
    
    # Convert filtered data to DataFrame
    df = pd.DataFrame(filtered_data)
    
    # Group data by minute and aggregate values (e.g., mean)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df = df.set_index('timestamp')
    df = df.resample('1T').mean().reset_index()
    
    # Convert DataFrame to JSON and return
    tabular_data = df.to_json(orient='records', date_format='iso')
    
    return tabular_data

if __name__ == '__main__':
    
    app.run(debug=True)
