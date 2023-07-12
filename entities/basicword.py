class BasicWord:
    """
    Represent a word
    """

    def __init__(self, word: str, subwords: list):
        """
        Create  word
        :param word: value (case-insensitive)
        :param subwords: list of subwords (case-insensitive)
        """

        self._subwords = [wrd.lower() for wrd in subwords]
        self._word = word.lower()

    def is_contains(self, subword: str) -> bool:
        """
        Check if word contains subword
        :param subword: checked subword (case-insensitive)
        :return: True if word contains subword, False otherwise
        """

        return subword.lower() in self._subwords

    @property
    def subwords_count(self) -> int:
        """
        Count of subwords
        :return:
        """

        return len(self._subwords)

    def __str__(self) -> str:
        return self._word

    def __repr__(self) -> str:
        return f'BasicWord(word={self._word}, subwords={self._subwords})'
