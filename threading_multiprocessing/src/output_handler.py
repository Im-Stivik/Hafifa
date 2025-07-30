import pandas

from threading_multiprocessing.consts import RESULT_FIELDS


class PandaCsv:
    def __init__(self, filename: str):
        self.filename = filename

    def write(self, data: pandas.DataFrame):
        data.index.name = 'timestamp'
        data['stock'] = data['Close']

        data = data.loc[:, RESULT_FIELDS]
        data.to_csv(self.filename)
