import os
import json
import random
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

    @unittest.mock.patch.object(random, 'shuffle')
    def test_get_word_generator(self, _):

        words_source = [
            BasicWord('word1', []),
            BasicWord('word2', [])
        ]

        word_generator = utils.get_word_generator(words_source)

        word1 = next(word_generator)
        word2 = next(word_generator)
        word3 = next(word_generator)

        self.assertIsInstance(word1, BasicWord)
        self.assertNotEqual(word1, word2)
        self.assertEqual(word1, word3)

    @unittest.mock.patch('utils.settings.STOP_WORDS', ['stop', 'СТОП'])
    def test_check_stop_word(self):
        self.assertTrue(utils.check_stop_word('стоп'))
        self.assertTrue(utils.check_stop_word('StOp'))
        self.assertFalse(utils.check_stop_word('SomeWord'))


if __name__ == '__main__':
    unittest.main()
