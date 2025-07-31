from concurrent.futures import ThreadPoolExecutor
from typing import List

from src.stock_settings import StockSettings
from src.io_handler import write_csv, read_times
from src.stock_retriever import StockRetriever

import pandas

def stock_pipeline(stock_settings: StockSettings):
    times = read_times(stock_settings.dates_file)
    stock = StockRetriever(stock_settings.stock_name)
    data: pandas.DataFrame = stock.get_stock_for_timestamp(times)

    write_csv(data,stock_settings.output_file)


def run_threaded_pipeline(stock_settings: List[StockSettings]):
    with ThreadPoolExecutor() as executor:
        executor.map(stock_pipeline, stock_settings)
