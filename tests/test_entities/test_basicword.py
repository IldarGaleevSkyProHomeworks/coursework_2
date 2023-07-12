import os
import json
import unittest

from entities import BasicWord


class BasicWordTestCase(unittest.TestCase):
    TEST_DIR = os.path.join(os.path.dirname(__file__), '..')

    def setUp(self) -> None:
        filename = os.path.join(self.TEST_DIR, 'data', 'test_data.json')
        with open(filename, 'r', encoding='utf-8') as file:
            self.json_test_data_item = json.load(file)[0]

        word = self.json_test_data_item['word']
        subwords = self.json_test_data_item['subwords']

        self.basic_word_instance_for_test = BasicWord(word, subwords)

    def test_subwords_count(self):
        required_subwords_count = len(self.json_test_data_item['subwords'])

        self.assertEqual(self.basic_word_instance_for_test.subwords_count, required_subwords_count)

    def test_is_contains_true(self):
        contained_subword = self.json_test_data_item['subwords'][0]

        self.assertTrue(self.basic_word_instance_for_test.is_contains(contained_subword))

    def test_is_contains_false(self):
        no_contained_subword = 'fakeWord'

        self.assertFalse(self.basic_word_instance_for_test.is_contains(no_contained_subword))

    def test_word_value(self):
        self.assertEqual(self.basic_word_instance_for_test.word, self.json_test_data_item['word'])


if __name__ == '__main__':
    unittest.main()
