import os
import json
import unittest


from datasource import DatasourceJsonFile


class DataSourceJsonFileTestCase(unittest.TestCase):
    TEST_DIR = os.path.join(os.path.dirname(__file__), '..')

    def setUp(self) -> None:
        filename = os.path.join(self.TEST_DIR, 'data', 'test_data.json')
        with open(filename, 'r', encoding='utf-8') as file:
            self.json_test_data_item = json.load(file)[0]

    def test_get_data(self):
        filename = os.path.join(self.TEST_DIR, 'data', 'test_data.json')
        required_word = self.json_test_data_item['word']
        required_subwords = self.json_test_data_item['subwords']

        data_source_instance_for_test = DatasourceJsonFile(filename)
        data_for_assert = data_source_instance_for_test.get_data()

        self.assertEqual(data_for_assert[0]['word'], required_word)
        self.assertEqual(data_for_assert[0]['subwords'], required_subwords)

    def test_get_data_none(self):
        filename = os.path.join(self.TEST_DIR, 'data', 'unknown.json')

        data_source_instance_for_test = DatasourceJsonFile(filename)

        data_for_assert = data_source_instance_for_test.get_data()

        self.assertEqual(data_for_assert, None)


if __name__ == '__main__':
    unittest.main()
