import os
from datetime import datetime
from requests_html import HTMLSession

class WeatherDataRetriever:
    @staticmethod
    def fetch_weather_html(query):
        """
        Fetches weather HTML from Google for a given location query.

        Parameters:
        - query (str): The location for which weather information is requested.

        Returns:
        - r.html: The HTML response containing weather information.
        """
        url = f"https://www.google.com/search?q=weather+{query}"

        try:
            s = HTMLSession()
            r = s.get(url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
            })

            return r.html
        except Exception as e:
            print(f"Error retrieving weather HTML: {e}")
            return None

    @staticmethod
    def get_weather_data(query):
        """
        Extracts weather data from HTML for a given location query.

        Parameters:
        - query (str): The location for which weather information is requested.

        Returns:
        - dict: A dictionary containing weather information.
        """
        html = WeatherDataRetriever.fetch_weather_html(query)

        if html is None:
            return {
                "status": False,
                "temp_max": None,
                "temp_min": None,
                "desc_day": None,
                "temp_current": None,
                "unit": None,
                "desc_current": None,
                "rain_current": None,
                "air_humidity_current": None,
                "wind_speed_current": None,
                "date_time": None
            }

        try:
            temp_max = html.find("div.wNE31c", first=True).find("span.wob_t")[0].text
            temp_min = html.find("div.wNE31c", first=True).find("span.wob_t")[-2].text
            desc_day = html.find("g-img.uW5pk", first=True).find("img#dimg_1", first=True).attrs.get("alt")
            temp_current = html.find("span#wob_tm", first=True).text
            unit = html.find("div.vk_bk.wob-unit span.wob_t", first=True).text
            desc_current = html.find("div.VQF4g", first=True).find("span#wob_dc", first=True).text
            rain_current = html.find("div.wtsRwe", first=True).find("span#wob_pp", first=True).text
            air_humidity_current = html.find("div.wtsRwe", first=True).find("span#wob_hm", first=True).text
            wind_speed_current = html.find("div.wtsRwe", first=True).find("span#wob_ws", first=True).text
            date_time = datetime.now()
            
            return {
                "status": True,
                "temp_max": temp_max,
                "temp_min": temp_min,
                "desc_day": desc_day,
                "temp_current": temp_current,
                "unit": unit,
                "desc_current": desc_current,
                "rain_current": rain_current,
                "air_humidity_current": air_humidity_current,
                "wind_speed_current": wind_speed_current,
                "date_time": date_time
            }
        except Exception as e:
            print(f"Error parsing weather data: {e}")
            return {
                "status": False,
                "temp_max": None,
                "temp_min": None,
                "desc_day": None,
                "temp_current": None,
                "unit": None,
                "desc_current": None,
                "rain_current": None,
                "air_humidity_current": None,
                "wind_speed_current": None,
                "date_time": None
            }

