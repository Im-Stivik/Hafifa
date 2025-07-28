from datetime import datetime
from typing import Dict, Any

import pandas
from yfinance import Market, Ticker


class StockRetriever:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.stock = Ticker(ticker=stock_name)

    def get_stock_for_timestamp(self, starting_date: datetime, end_date: datetime):
        stock_data = self.stock.history(start=starting_date, end=end_date, interval='1h').to_dict()
        formated_data = self.__group_by_timestamp(stock_data)

        return map(lambda timestamp, data: self.__get_relevant_data(timestamp, data), formated_data.keys(), formated_data.values())

    @staticmethod
    def __group_by_timestamp(stock_history: Dict[str, Dict[str, Dict[pandas.Timestamp, Any]]]) -> Dict[str, Any]:
        result = dict()

        for field_name, values in stock_history.items():
            for timestamp, value in values.items():
                timestamp = str(timestamp)
                result.setdefault(timestamp, dict())
                result[timestamp][field_name] = value

        return result

    @staticmethod
    def __get_relevant_data(timestamp, full_data) -> Dict[str, Any]:
        return {
            'timestamp': timestamp,
            'stock': full_data['Open'],
            "percentage_change": ((full_data['Close'] - full_data['Open']) / full_data['Open']) * 100,
        }
