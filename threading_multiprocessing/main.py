from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from typing import Iterable, Dict, Any

from src.stock_retriever import StockRetriever
import csv

from threading_multiprocessing.consts import SETTINGS


def write_output_to_csv(data: Iterable[Dict[str, Any]], filename: str):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'stock', 'percentage_change']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

def get_stocks(stock_settings: Dict[str, Any]):
    times = []

    with open(stock_settings['dates']) as file:
        times = file.read().split('\n')[:-1]

    times = list(map(lambda time: datetime.fromisoformat(time), times))
    stock = StockRetriever(stock_settings['name'])
    data = stock.get_stock_for_timestamp(times)

    write_output_to_csv(data, stock_settings['output'])

def main():
    with ThreadPoolExecutor() as executor:
        executor.map(get_stocks, SETTINGS.values())

if __name__ == '__main__':
    main()