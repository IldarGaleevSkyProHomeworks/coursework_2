class Player:
    """
    Represent a player
    """

    def __init__(self, name: str):
        """
        Create a player
        :param name: player name
        """

        self._name = name
        self._usedwords = []

    def is_usedword(self, word: str) -> bool:
        """
        Check if word is used
        :param word: checked word
        :return: True if word is used, False otherwise
        """

        return word.lower() in self._usedwords

    def add_usedword(self, word: str):
        """
        Add word to used words
        :param word:
        """

        self._usedwords.append(word.lower())

    @property
    def usedwords_count(self) -> int:
        """
        Count of used words
        :return:
        """

        return len(self._usedwords)

    def __str__(self) -> str:
        return self._name

    def __repr__(self) -> str:
        return f'Player(name={self._name}, usedwords={self._usedwords})'
