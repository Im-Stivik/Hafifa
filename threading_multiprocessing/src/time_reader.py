from datetime import datetime
from typing import List


class TimeFileReader:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def read(self) -> List[datetime]:
        times = []

        with open(self.stock_settings.dates_file) as file:
            times = file.read().split('\n')[:-1]

        times = [datetime.fromisoformat(time) for time in times]

        return times
