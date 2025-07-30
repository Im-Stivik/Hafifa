from datetime import datetime, timezone
from typing import Dict, Any, List, Iterable

import pandas
from yfinance import Ticker


class StockRetriever:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.stock = Ticker(ticker=stock_name)

    def get_stock_for_timestamp(self, timestamps: List[datetime]) -> pandas.DataFrame:
        starting_date = min(timestamps)
        end_date = max(timestamps)
        stock_data = self.stock.history(start=starting_date, end=end_date, interval='1h')
        stock_data = stock_data[stock_data.index.isin(timestamps)]
        stock_data['percentage_change'] = (stock_data['Open'] - stock_data['Close']) / stock_data['Open'] * 100

        return stock_data