from os import environ
from typing import List

from threading_multiprocessing.src.stock_settings import StockSettings, load_stock_settings_from_env

SETTINGS: List[StockSettings] = load_stock_settings_from_env()

RESULT_FIELDS = ['stock', 'percentage_change']