import os
import json
import unittest.mock

import datasource
import utils
from entities import BasicWord


class UtilsTestCase(unittest.TestCase):
    TEST_DIR = os.path.dirname(__file__)

    def setUp(self) -> None:
        filename = os.path.join(self.TEST_DIR, 'data', 'test_data.json')
        with open(filename, 'r', encoding='utf-8') as file:
            self.json_data_test = json.load(file)

    @unittest.mock.patch.object(datasource.DataSourceJsonKeeper, 'get_data', return_value=None)
    @unittest.mock.patch.object(datasource.DatasourceJsonFile, 'get_data')
    def test_get_data_from_jsonfile(self, _, data_source_json_file_mock):
        data_source_json_file_mock.return_value = self.json_data_test
        data = utils.get_data()
        self.assertIsInstance(data, (list, BasicWord))

    @unittest.mock.patch.object(datasource.DataSourceJsonKeeper, 'get_data', return_value=None)
    @unittest.mock.patch.object(datasource.DatasourceJsonFile, 'get_data', return_value=None)
    def test_get_data_raises_exception(self, *_):
        with self.assertRaises(Exception) as context:
            utils.get_data()

        self.assertEqual(context.exception.args[0], 'Data not found')


if __name__ == '__main__':
    unittest.main()
