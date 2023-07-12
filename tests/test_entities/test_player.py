import unittest

from entities import Player


class PlayerTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.player_tested_instance = Player('Test')

    def test_player_add_usedword_and_is_usedword_true(self):
        self.player_tested_instance.add_usedword('test')
        self.assertTrue(self.player_tested_instance.is_usedword('test'))

    def test_player_is_usedword_false(self):
        self.assertFalse(self.player_tested_instance.is_usedword('fakeWord'))


if __name__ == '__main__':
    unittest.main()
