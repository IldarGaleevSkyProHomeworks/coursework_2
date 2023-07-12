import datasource.datasource as ds
import requests


class DataSourceJsonKeeper(ds.DataSource):
    """
    Provide data from jsonkeeper.com
    """

    _JSON_KEEPER_URL = 'https://www.jsonkeeper.com/b/'

    def __init__(self, file_id: str):
        """
        :param file_id: File id from jsonkeeper.com
        """

        super().__init__()
        self._file_id = file_id

    def get_data(self) -> list | None:
        request = requests.get(self._JSON_KEEPER_URL + self._file_id)
        if request.status_code == 200:
            self._data = request.json()
        return super().get_data()

