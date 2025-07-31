from concurrent.futures import ThreadPoolExecutor
from typing import List

from src.stock_settings import StockSettings
from src.output_handler import PandaCsv
from src.stock_retriever import StockRetriever

from datetime import datetime
import pandas

class GetStockPipeline:
    def __init__(self, stock_settings: StockSettings):
        self.stock_settings = stock_settings

    def run(self):
        output = PandaCsv(self.stock_settings.output_file)
        times = []

        with open(self.stock_settings.dates_file) as file:
            times = file.read().split('\n')[:-1]

        times = list(map(lambda time: datetime.fromisoformat(time), times))
        stock = StockRetriever(self.stock_settings.stock_name)
        data: pandas.DataFrame = stock.get_stock_for_timestamp(times)

        output.write(data)

def run_threaded_pipeline(stock_settings: List[StockSettings]):
    with ThreadPoolExecutor() as executor:
        executor.map(lambda setting: GetStockPipeline(setting).run(), stock_settings)
