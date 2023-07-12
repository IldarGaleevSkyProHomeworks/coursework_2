import os
import json
import responses
import unittest

from datasource import DataSourceJsonKeeper


class DataSourceJsonKeeperTestCase(unittest.TestCase):
    TEST_DIR = os.path.join(os.path.dirname(__file__), '..')

    def setUp(self) -> None:
        filename = os.path.join(self.TEST_DIR, 'data', 'test_data.json')
        with open(filename, 'r', encoding='utf-8') as file:
            self.json_data_test = json.load(file)
            self.json_data_test_single_item = self.json_data_test[0]

    @responses.activate
    def test_get_data(self):
        jsonkeeper_file_id = 'TEST'

        responses.add(
            responses.GET,
            f'{DataSourceJsonKeeper._JSON_KEEPER_URL}{jsonkeeper_file_id}',
            json=self.json_data_test,
            status=200
        )

        required_word = self.json_data_test_single_item['word']
        required_subwords = self.json_data_test_single_item['subwords']

        data_source_instance_for_test = DataSourceJsonKeeper(jsonkeeper_file_id)

        data_for_assert = data_source_instance_for_test.get_data()

        self.assertEqual(data_for_assert[0]['word'], required_word)
        self.assertEqual(data_for_assert[0]['subwords'], required_subwords)

    @responses.activate
    def test_get_data_none(self):
        jsonkeeper_file_id = 'UNKNOWN'

        responses.add(
            responses.GET,
            f'{DataSourceJsonKeeper._JSON_KEEPER_URL}{jsonkeeper_file_id}',
            status=404
        )

        data_source_instance_for_test = DataSourceJsonKeeper(jsonkeeper_file_id)

        data_for_assert = data_source_instance_for_test.get_data()

        self.assertEqual(data_for_assert, None)


if __name__ == '__main__':
    unittest.main()
