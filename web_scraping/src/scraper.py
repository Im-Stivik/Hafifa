import requests
from src.html_parser import SoupHTMLParser
from src.screenshot import HTMLWebShotEngine
from consts import SCREENSHOT_NAME, OUTPUT_PATH, OUTPUT_JSON_FILE_NAME
from src.scraping_data import ScrapingData
import pathlib
import json


class WebScraper:
    def __init__(self, url: str, url_parser=SoupHTMLParser, screenshot_engine=HTMLWebShotEngine):
        self.url = url
        self.url_parser = url_parser
        self.screenshot_engine = screenshot_engine()

    def scrape(self):
        save_path: pathlib.Path = self.__create_output_path()

        result = ScrapingData()

        result.html = self.__get_html_content()
        result.resources = self.url_parser(result.html).get_all_urls()
        result.set_screenshot(self.screenshot_engine.take_screenshot(
            self.url, save_path / SCREENSHOT_NAME))

        self.__save_output(result)

        return result

    def __get_html_content(self) -> str:
        return requests.get(self.url).text

    def __create_output_path(self) -> pathlib.Path:
        fixed_url = self.__fix_path_name_of_url(self.url)
        path = pathlib.Path(f"{OUTPUT_PATH}/{fixed_url}")
        path.mkdir(parents=True, exist_ok=True)

        return pathlib.Path(path)

    def __save_output(self, output: ScrapingData):
        fixed_url = self.__fix_path_name_of_url(self.url)
        path = pathlib.Path(OUTPUT_PATH) / pathlib.Path(fixed_url) / \
               pathlib.Path(OUTPUT_JSON_FILE_NAME)
        with open(path, 'w') as file:
            data = output.model_dump()
            json.dump(data, file, ensure_ascii=False)

    @staticmethod
    def __fix_path_name_of_url(url: str) -> str:
        """
            this function takes the http://url and only given the url
            this is done becuase the // is a folder so its interfiring
        """
        return url.split('https://')[-1].split('http://')[-1]
