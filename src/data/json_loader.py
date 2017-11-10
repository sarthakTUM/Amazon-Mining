import gzip

import pandas as pd

from src.data.loader import Loader


class JSONLoader(Loader):
    def __init__(self, read_mode='rb'):
        self.read_mode = read_mode

    def load_data(self, file_name):
        """
        code partly taken from: http://jmcauley.ucsd.edu/data/amazon/
        :param file_name: complete path to open
        :return: pandas dataframe
        """
        try:
            i = 0
            df = {}
            for d in self._parse(file_name):
                df[i] = d
                i += 1
            return pd.DataFrame.from_dict(df, orient='index')
        except Exception as e:
            raise e

    def _parse(self, file_name):
        g = gzip.open(file_name, self.read_mode)
        for l in g:
            yield eval(l)
