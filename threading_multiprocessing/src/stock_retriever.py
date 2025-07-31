from datetime import datetime
from typing import List
import pandas
from yfinance import Ticker

from consts import STOCK_TIME_INTERVAL


def percentage_change(start, end):
    """
    this function calculates the percentage that the value have changes from the start to the end
    :param start: what the value was before the change
    :param end: the value after the change
    :return: how much the value was changed in percentage
    """
    return (end - start) / start * 100


class StockRetriever:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.stock = Ticker(ticker=stock_name)

    def get_stock_for_timestamp(self, timestamps: List[datetime]) -> pandas.DataFrame:
        starting_date = min(timestamps)
        end_date = max(timestamps)
        stock_data = self.stock.history(start=starting_date, end=end_date, interval=STOCK_TIME_INTERVAL)
        stock_data = stock_data[stock_data.index.isin(timestamps)]
        stock_data['percentage_change'] = percentage_change(stock_data['Open'], stock_data['Close'])

        return stock_data
