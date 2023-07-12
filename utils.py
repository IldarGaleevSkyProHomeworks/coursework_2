import random
from collections.abc import Generator

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
        f'Составьте {word.subwords_count} слов из слова {word.word.upper()}\n'
        f'Слова должны быть не короче {settings.MIN_WORD_LENGTH} букв\n'
        f'Чтобы закончить игру, угадайте все слова или напишите одно из слов: {stop_words_str}')
