from datetime import datetime
from typing import List

import pandas

from consts import RESULT_FIELDS


def write_csv(data: pandas.DataFrame, filename: str):
    data.index.name = 'timestamp'
    data['stock'] = data['Close']

    data = data.loc[:, RESULT_FIELDS]
    data.to_csv(filename)


def read_times(filename: str) -> List[datetime]:
    df = pandas.read_csv(filename, header=None)
    return pandas.to_datetime(df.iloc[:-1, 0]).to_list()
