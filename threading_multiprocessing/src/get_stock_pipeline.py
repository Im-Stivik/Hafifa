from concurrent.futures import ThreadPoolExecutor
from typing import List

from src.stock_settings import StockSettings
from src.output_handler import PandaCsv
from src.stock_retriever import StockRetriever

from datetime import datetime
import pandas

from src.time_reader import TimeFileReader


class GetStockPipeline:
    def __init__(self, stock_settings: StockSettings):
        self.stock_settings = stock_settings

    def run(self):
        times = TimeFileReader(self.stock_settings.dates_file).read()
        stock = StockRetriever(self.stock_settings.stock_name)
        data: pandas.DataFrame = stock.get_stock_for_timestamp(times)

        PandaCsv(self.stock_settings.output_file).write(data)

def run_threaded_pipeline(stock_settings: List[StockSettings]):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda setting: GetStockPipeline(setting).run(), stock_settings)
