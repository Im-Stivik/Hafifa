from datetime import datetime
from typing import Iterable, Dict, Any

from src.stock_retriever import StockRetriever
import csv

def write_output_to_csv(data: Iterable[Dict[str, Any]], filename: str):
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['timestamp', 'stock', 'percentage_change']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)

dates_file = 'bitcoin_dates.txt'

def get_stocks_for(stock_name: str):
    times = []

    with open(dates_file) as file:
        times = file.read().split('\n')[:-1]

    times = list(map(lambda time: datetime.fromisoformat(time), times))
    stock = StockRetriever(stock_name)
    data = stock.get_stock_for_timestamp(times)

    write_output_to_csv(data, 'output.csv')

def main():
    get_stocks_for('BTC-USD')


if __name__ == '__main__':
    main()