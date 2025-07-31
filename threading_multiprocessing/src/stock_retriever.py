from datetime import datetime
from typing import List
import pandas
from yfinance import Ticker

from src.utils import percentage_change


class StockRetriever:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.stock = Ticker(ticker=stock_name)

    def get_stock_for_timestamp(self, timestamps: List[datetime]) -> pandas.DataFrame:
        starting_date = min(timestamps)
        end_date = max(timestamps)
        stock_data = self.stock.history(start=starting_date, end=end_date, interval='1h')
        stock_data = stock_data[stock_data.index.isin(timestamps)]
        stock_data['percentage_change'] = percentage_change(stock_data['Open'], stock_data['Close'])

        return stock_data