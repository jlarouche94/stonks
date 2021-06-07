"""

"""
import requests

TIME_SERIES_INTRADAY = 'TIME_SERIES_INTRADAY'

class StonksApi():
    """
    Class for calling and processing API requests from alphavantage
    """
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.base_url = 'https://www.alphavantage.co'

    def format_url(self, stock_name, func_name=TIME_SERIES_INTRADAY):
        """
        """
        return f"{self.base_url}/query?function={func_name}&symbol={stock_name}&interval=15min&apikey={self.api_key}"
    
    def get_time_series(self, stock_name):
        """
        """
        uri = self.format_url(stock_name=stock_name, func_name=TIME_SERIES_INTRADAY)
        res = requests.get(uri)
        res.raise_for_status()
        json_data = res.json()
        print(res.json())
        return json_data