from datetime import datetime, timezone
from typing import Dict, Any, List, Iterable

import pandas
from yfinance import Market, Ticker
from src.stock_data import StockData, Relevant


class StockRetriever:
    def __init__(self, stock_name: str):
        self.stock_name = stock_name
        self.stock = Ticker(ticker=stock_name)

    def get_stock_for_timestamp(self, timestamps: List[datetime]) -> Iterable[Relevant]:
        starting_date = min(timestamps)
        end_date = max(timestamps)
        stock_data = self.stock.history(start=starting_date, end=end_date, interval='1h').to_dict()
        formated_data = self.__group_by_timestamp(stock_data)
        formated_data = list(map(lambda data: StockData(**data), formated_data.values()))
        formated_data = list(filter(lambda data: datetime.fromisoformat(data.timestamp).astimezone(timezone.utc) in timestamps, formated_data))

        return map(lambda data: data.get_relevant_data(), formated_data)

    @staticmethod
    def __group_by_timestamp(stock_history: Dict[str, Dict[str, Dict[pandas.Timestamp, Any]]]) -> Dict[str, Any]:
        result = dict()

        for field_name, values in stock_history.items():
            for timestamp, value in values.items():
                timestamp = str(timestamp)
                result.setdefault(timestamp, dict())
                result[timestamp][field_name] = value

        for timestamp in result.keys():
            result[timestamp]['timestamp'] = timestamp

        return result

    @staticmethod
    def __get_relevant_data(timestamp, full_data) -> Dict[str, Any]:
        return {
            'timestamp': timestamp,
            'stock': full_data['Open'],
            "percentage_change": ((full_data['Close'] - full_data['Open']) / full_data['Open']) * 100,
        }
