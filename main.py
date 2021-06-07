"""
Entry point
"""
from stonks_api import StonksApi
from data import TimeSeriesData

API_KEY = 'U9ONJQWNZK9UWCO5'

def main():
    """
    Main
    """
    api = StonksApi(api_key=API_KEY)
    data = api.get_time_series(stock_name='IBM')
    time_series = TimeSeriesData(data=data)

if __name__ == '__main__':
    main()