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

def main():
    stock = StockRetriever('BTC-USD')

    starting_time = datetime.fromisoformat('2025-03-17 19:00')
    ending_time = datetime.fromisoformat('2025-06-15 13:00')

    data = stock.get_stock_for_timestamp(starting_time, ending_time)
    write_output_to_csv(data, 'output.csv')


if __name__ == '__main__':
    main()