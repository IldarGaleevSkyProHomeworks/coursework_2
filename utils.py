import random
from collections.abc import Generator

import settings
import datasource
import entities

# ANSI Escape Sequences
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
ESC_FG = '\x1B[38;5;{}m'
FG_RED = ESC_FG.format(1)
FG_GREEN = ESC_FG.format(2)
FG_YELLOW = ESC_FG.format(3)
FG_MAGENTA = ESC_FG.format(5)
FG_RESET = '\x1B[0m'


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


def get_player() -> entities.Player:
    while True:
        player_name = input('Введите имя игрока: ').strip()
        if player_name:
            break
        else:
            print('Имя не может быть пустым!')

    player = entities.Player(player_name)
    return player


def get_word_generator(words_source: list[entities.BasicWord]) -> Generator[entities.BasicWord]:
    word_pool = []
    while True:
        if not word_pool:
            word_pool = words_source.copy()
            random.shuffle(word_pool)

        yield word_pool.pop()


def print_word_prompt(word: entities.BasicWord) -> None:
    stop_words_str = ', '.join([f'"{w}"' for w in settings.STOP_WORDS])
    print(
        f'Составьте {FG_GREEN}{word.subwords_count}{FG_RESET} слов из слова {FG_GREEN}{word.word.upper()}{FG_RESET}\n'
        f'Слова должны быть не короче {FG_MAGENTA}{settings.MIN_WORD_LENGTH}{FG_RESET} букв\n'
        f'Чтобы закончить игру, угадайте все слова или напишите одно из слов: {stop_words_str}')


def check_stop_word(word_str: str) -> bool:
    return word_str.lower() in [wrd.lower() for wrd in settings.STOP_WORDS]


def check_user_input(user_input: str) -> bool:
    return len(user_input) >= settings.MIN_WORD_LENGTH


def check_word(player: entities.Player, word: entities.BasicWord, subword_str: str) -> bool | None:
    """
    Checking word
    :param player: player
    :param word: word object
    :param subword_str: checked word
    :return: 'True' if the word contains subword_str, 'False' otherwise. 'None' if already used
    """

    if player.is_usedword(subword_str):
        return None

    if word.is_contains(subword_str):
        player.add_usedword(subword_str)
        return True

    return False
