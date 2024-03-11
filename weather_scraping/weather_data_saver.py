import os
import time
from datetime import datetime
from .weather_data_retriever import WeatherDataRetriever

class WeatherDataSaver:
    @staticmethod
    def save_to_csv(data, data_file_path, logs_file_path, user, execution_time):
        """
        Saves weather data to a CSV file and logs the operation.

        Parameters:
        - data (dict): Weather data to be saved.
        - data_file_path (str): Path to the CSV file for weather data.
        - logs_file_path (str): Path to the CSV file for logs.
        - user (str): User information.
        - execution_time (float): Execution time of the main function.

        Returns:
        - None
        """
        # Create data directory if not exists
        path = os.curdir
        data_path = os.path.join(path, 'data')
        os.makedirs(data_path, exist_ok=True)
        
        # Check if logs file exists, if not, create it
        if not os.path.exists(logs_file_path):
            with open(logs_file_path, 'w', encoding='utf-8') as logs_file:
                print("user,execution_time,status", file=logs_file)
        
        if not os.path.exists(data_file_path):
            with open(data_file_path, 'w', encoding='utf-8') as data_file:
                print("air_humidity_current,desc_current,desc_day,unit,rain_current,temp_current,temp_max,temp_min,wind_speed_current,date_time", file=data_file)

        with open(data_file_path, 'a', encoding='utf-8') as file:
            if data['status']:
                print(f"{data['air_humidity_current']},{data['desc_current']},{data['desc_day']},{data['unit']},{data['rain_current']},{data['temp_current']},{data['temp_max']},{data['temp_min']},{data['wind_speed_current']},{data['date_time']}", file=file)
            else:
                print(f"{False},{None},{None},{None},{None},{None},{None},{None},{None},{None}", file=file)

        with open(logs_file_path, "a", encoding='utf-8') as file:
            print(f"{user},{execution_time},{data['status']}", file=file)
