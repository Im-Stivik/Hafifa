from os import environ

from threading_multiprocessing.src.stock_settings import StockSettings

BITCOIN_STOCK_NAME = 'BTC-USD'
BITCOIN_OUTPUT_FILE = environ.get('BITCOIN_OUTPUT_FILE')
BITCOIN_DATES_FILE = environ.get('BITCOIN_DATES_FILE')

AMAZON_STOCK_NAME = 'AMZN'
AMAZON_OUTPUT_FILE = environ.get('AMAZON_OUTPUT_FILE')
AMAZON_DATES_FILE = environ.get('AMAZON_DATES_FILE')

GOOGLE_STOCK_NAME = 'GOOG'
GOOGLE_OUTPUT_FILE = environ.get('GOOGLE_OUTPUT_FILE')
GOOGLE_DATES_FILE = environ.get('GOOGLE_DATES_FILE')


SETTINGS = [
    StockSettings(name='bitcoin', stock_name=BITCOIN_STOCK_NAME, output_file=BITCOIN_OUTPUT_FILE, dates_file=BITCOIN_DATES_FILE),
    StockSettings(name='amazon', stock_name=AMAZON_STOCK_NAME, output_file=AMAZON_OUTPUT_FILE, dates_file=AMAZON_DATES_FILE),
    StockSettings(name='google', stock_name=GOOGLE_STOCK_NAME, output_file=GOOGLE_OUTPUT_FILE, dates_file=GOOGLE_DATES_FILE),
]

RESULT_FIELDS = ['timestamp', 'stock', 'percentage_change']