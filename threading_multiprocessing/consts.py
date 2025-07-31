import json
from os import environ
from typing import List

from src.stock_settings import StockSettings, load_stock_settings_from_env

SETTINGS_ENV_FILES = json.loads(environ.get('SETTINGS_ENV_FILES'))

SETTINGS: List[StockSettings] = [
    StockSettings(_env_file=env_file) for env_file in SETTINGS_ENV_FILES
]

STOCK_TIME_INTERVAL = '1h'

RESULT_FIELDS = ['stock', 'percentage_change']