class DataSource:
    """
    Basic class for data source
    """
    def __init__(self):
        self._data = None

    def get_data(self) -> list | None:
        """
        Returns data
        :return: a list with data or None if data could not be retrieved
        """

        return self._data

    def __repr__(self):
        return f'DataSource(_data={self._data})'

    def __str__(self):
        return ''.join([word['word'] for word in self._data])
