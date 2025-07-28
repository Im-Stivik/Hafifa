from concurrent.futures import ThreadPoolExecutor
from src.input_reader import FileLineReader
from src.scraper import WebScraper
from consts import INPUT_FILE, SCREENSHOT_NAME


def scrape_url(url: str):
    scraper = WebScraper(url)
    scraper.scrape()


if __name__ == "__main__":
    input = FileLineReader(INPUT_FILE)
    urls = input.get_input()

    with ThreadPoolExecutor() as executor:
        executor.map(scrape_url, urls)
