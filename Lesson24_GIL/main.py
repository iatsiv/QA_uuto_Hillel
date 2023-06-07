"""
1 Create custom thread for functions with and without parameters
2 Run tests in parallel using the pytest-xdist"""

from threading import Thread


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, daemon=None, id=None):
        super().__init__(group=group, target=target, name=name, args=args, kwargs=kwargs, daemon=daemon)
        self._target = target
        self.__id = id

    def run(self):
        print(f"\nfrom custom thread, id = {self.__id}")
        super().run()

def get_word_with_cyrillic_o():
    while True:
        input_word = input('Треба ввести слово, яке містить кирилічну літеру "о": ')
        text = input_word.isalpha()
        digit = input_word.isdigit()
        not_letter = len(input_word) > 1
        letter = len(input_word) == 1
        nothing = len(input_word) == 0
        cyr_symbol = 'о'
        lat_symbol = 'o'

        if text and not_letter and cyr_symbol in input_word.lower():
            print(f'Дякую! Введено слово "{input_word}", яке містить літеру "о"')
            return input_word

        elif text and letter:
            print(f'Введено "{input_word}", це літера, а не слово, давайте ще раз')

        elif digit:
            print(f'Введено "{input_word}", це число, а не слово, ще спробуй')

        elif text and cyr_symbol not in input_word.lower():
            print(f'Введено "{input_word}", тут немає кириличної "о", гарна спроба')

        elif text and lat_symbol in input_word.lower():
            print(f'Введено "{input_word}", яке містить "о" з латинки, а треба кириличну')

        elif nothing:
            print(f'Нічого не введено, а очікується слово з літерою "о"')

        else:
            print(f'Введено "{input_word}", це не слово, в слові допустимі лише літери ;)')

get_word_with_cyrillic_o_thread = CustomThread(target=get_word_with_cyrillic_o, id=1)
get_word_with_cyrillic_o_thread.start()

def fun_math(data1, data2):
    if isinstance(data1, bool) and isinstance(data2, bool):
        result = (data1, data2)
    elif isinstance(data1, (int, float)) and isinstance(data2, (int, float)):
        result = data1 * data2
    elif isinstance(data1, str) and isinstance(data2, str):
        result = data1 + data2
    else:
        result = (data1, data2)
    print(result)

fun_math_thread = CustomThread(target=fun_math, args=(3, 6), id=2)
fun_math_thread.start()
