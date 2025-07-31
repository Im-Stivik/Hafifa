from consts import SETTINGS
from src.get_stock_pipeline import run_threaded_pipeline

def main():
    run_threaded_pipeline(SETTINGS)

if __name__ == '__main__':
    main()