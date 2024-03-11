import os
import time
from datetime import datetime
from weather_scraping import WeatherDataRetriever, WeatherDataSaver

def main():
    """
    Main function to retrieve weather data, save it to CSV, and log the operation.
    """
    initial_time = time.time()
    
    query = "cacador sc"
    weather_data = WeatherDataRetriever.get_weather_data(query)

    final_time = time.time()
    execution_time = final_time - initial_time

    user = os.environ.get('USER') or os.environ.get('USERNAME')

    path = os.curdir
    data_path = os.path.join(path, 'data')
    os.makedirs(data_path, exist_ok=True)

    data_file_path = os.path.join(data_path, 'weather_report_data.csv')

    logs_file_path = os.path.join(data_path, 'logs.csv')

    WeatherDataSaver.save_to_csv(weather_data, data_file_path, logs_file_path, user, execution_time)

if __name__ == "__main__":
    main()

