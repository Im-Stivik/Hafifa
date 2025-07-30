from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import Iterable, Dict, Any

from src.stock_retriever import StockRetriever
import csv

from threading_multiprocessing.consts import SETTINGS, RESULT_FIELDS
from threading_multiprocessing.src.stock_settings import StockSettings


def write_output_to_csv(data: Iterable[Dict[str, Any]], filename: str):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=RESULT_FIELDS)

        writer.writeheader()
        writer.writerows(data)

def get_stocks(stock_settings: StockSettings):
    times = []

    with open(stock_settings.dates_file) as file:
        times = file.read().split('\n')[:-1]

    times = list(map(lambda time: datetime.fromisoformat(time), times))
    stock = StockRetriever(stock_settings.stock_name)
    data = stock.get_stock_for_timestamp(times)

    write_output_to_csv(data, stock_settings.output_file)

def main():
    with ThreadPoolExecutor() as executor:
        executor.map(get_stocks, SETTINGS)

if __name__ == '__main__':
    main()