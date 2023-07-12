import utils


def main(data_list: list):

    for word in data_list:
        print(word)


if __name__ == '__main__':
    try:
        data = utils.get_data()
        main(data)
    except Exception as e:
        print("Ооооой! Что-то пошло не так 😥")
        print("Ошибочка вышла: ", e)
