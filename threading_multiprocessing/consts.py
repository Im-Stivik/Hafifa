from os import environ

BITCOIN_STOCK_NAME = 'BTC-USD'
BITCOIN_OUTPUT_FILE = environ.get('BITCOIN_OUTPUT_FILE')
BITCOIN_DATES_FILE = environ.get('BITCOIN_DATES_FILE')

AMAZON_STOCK_NAME = 'AMZN'
AMAZON_OUTPUT_FILE = environ.get('AMAZON_OUTPUT_FILE')
AMAZON_DATES_FILE = environ.get('AMAZON_DATES_FILE')

GOOGLE_STOCK_NAME = 'GOOG'
GOOGLE_OUTPUT_FILE = environ.get('GOOGLE_OUTPUT_FILE')
GOOGLE_DATES_FILE = environ.get('GOOGLE_DATES_FILE')

SETTINGS = {
    'bitcoin': {
        'name': BITCOIN_STOCK_NAME,
        'output': BITCOIN_OUTPUT_FILE,
        'dates': BITCOIN_DATES_FILE
    },
    'amazon': {
        'name': AMAZON_STOCK_NAME,
        'output': AMAZON_OUTPUT_FILE,
        'dates': AMAZON_DATES_FILE
    },
    'google': {
        'name': GOOGLE_STOCK_NAME,
        'output': GOOGLE_OUTPUT_FILE,
        'dates': GOOGLE_DATES_FILE
    }
}