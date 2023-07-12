import settings
import datasource
import entities


def get_data() -> list[entities.BasicWord]:
    """
    Getting data
    :return: a list of BasicWord
    :raises Exception: if data could not be retrieved
    """

    data_source = datasource.DataSourceJsonKeeper(settings.DATA_JSON_KEEPER_FILE_ID)
    data_result = data_source.get_data()

    if data_result is None:
        data_source = datasource.DatasourceJsonFile(settings.DATA_JSON_FILENAME)
        data_result = data_source.get_data()

    if data_result is None:
        raise Exception('Data not found')

    return [entities.BasicWord(word_item['word'], word_item['subwords']) for word_item in data_result]
