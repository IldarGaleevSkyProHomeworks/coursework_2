import os

import datasource.datasource as ds
import json


class DataSourceJsonFile(ds.DataSource):
    """
    Provide data from json file
    """

    def __init__(self, file_name: str):
        """
        :param file_name: Path to json file
        """

        super().__init__()
        self._file_name = file_name

    def get_data(self) -> list:
        if os.path.exists(self._file_name):
            with open(self._file_name, 'r', encoding='utf-8') as file:
                self._data = json.load(file)
        return self._data
