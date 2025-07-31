import os
import re
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from typing import List


class StockSettings(BaseSettings):
    stock_name: str
    output_file: str
    dates_file: str


def load_stock_settings_from_env() -> List[StockSettings]:
    stock_data = {}

    # Pattern: BITCOIN_STOCK_NAME, ETHEREUM_OUTPUT_FILE, etc.
    pattern = re.compile(r'^([A-Z0-9_]+)_(STOCK_NAME|OUTPUT_FILE|DATES_FILE)$')

    for key, value in os.environ.items():
        match = pattern.match(key)
        if not match:
            continue

        stock_key, field_type = match.groups()
        stock_key = stock_key.upper()

        if stock_key not in stock_data:
            stock_data[stock_key] = {"name": stock_key}

        field_map = {
            "STOCK_NAME": "stock_name",
            "OUTPUT_FILE": "output_file",
            "DATES_FILE": "dates_file"
        }

        stock_data[stock_key][field_map[field_type]] = value

    settings = []
    for stock_key, fields in stock_data.items():
        try:
            settings.append(StockSettings(**fields))
        except Exception as e:
            print(f"Skipping {stock_key}: {e}")  # Optionally handle validation errors here

    return settings