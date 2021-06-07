"""
"""
import numpy as np
import pandas as pd

class TimeSeriesData():
    """
    """
    def __init__(self, data):
        """
        Create pandas data models
        """
        times_series = self._convert_to_time_series(data=data)

    def _convert_to_time_series(self, data):
        """
        """
        import pdb; pdb.set_trace()
        dates = [key for key, value in data['Time Series (15min)'].items()]
        pd_date = pd.to_datetime(dates[0])
