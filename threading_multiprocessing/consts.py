from os import environ

BITCOIN_STOCK_NAME = 'BTC-USD'
BITCOIN_OUTPUT_FILE = environ.get('BITCOIN_OUTPUT_FILE')
BITCOIN_DATES_FILE = environ.get('BITCOIN_DATES_FILE')

SETTINGS = {
    'bitcoin': {
        'name': BITCOIN_STOCK_NAME,
        'output': BITCOIN_OUTPUT_FILE,
        'dates': BITCOIN_DATES_FILE
    }
}