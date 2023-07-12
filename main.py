import utils


def main(data_list: list):
    is_game_running = True

    player = utils.get_player()
    words_generator = utils.get_word_generator(data_list)

    print(f'Привет, {player}\n')

    while is_game_running:
        word = next(words_generator)
        subword_count = word.subwords_count

        utils.print_word_prompt(word)

        print('-' * 10)

        while subword_count:
            user_input = input('Ваше слово: ').lower().strip()

            if not utils.check_user_input(user_input):
                print('Слишком короткое слово')
                continue

            if utils.check_stop_word(user_input):
                is_game_running = False
                print(f'{utils.FG_YELLOW}Вы угадали {player.usedwords_count} слов!{utils.FG_RESET}')
                break

            match utils.check_word(player, word, user_input):
                case None:
                    print(f'{utils.FG_YELLOW}Уже использовано!{utils.FG_RESET}')
                case True:
                    subword_count -= 1
                    print(f'{utils.FG_GREEN}Правильно!{utils.FG_RESET}')
                case False:
                    print(f'{utils.FG_RED}Неправильно!{utils.FG_RESET}')

            if subword_count:
                print(f'Осталось {utils.FG_MAGENTA}{subword_count}{utils.FG_RESET} слов\n')
            else:
                print("Вы молодец! Продолжим!")

        print('-' * 10)

    print(f'Спасибо за игру, {player}')


if __name__ == '__main__':
    try:
        data = utils.get_data()
        main(data)
    except Exception as e:
        print("Ооооой! Что-то пошло не так 😥")
        print("Ошибочка вышла: ", e)
