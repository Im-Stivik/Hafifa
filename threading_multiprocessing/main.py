from datetime import datetime
from src.stock_retriever import StockRetriever

def main():
    stock = StockRetriever('BTC-USD')

    starting_time = datetime.fromisoformat('2025-03-17 19:00')
    ending_time = datetime.fromisoformat('2025-06-15 13:00')

    test = list(stock.get_stock_for_timestamp(starting_time, ending_time))
    print(test)


if __name__ == '__main__':
    main()