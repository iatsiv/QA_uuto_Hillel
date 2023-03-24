'''1. Напишіть цикл, який буде вимагати від користувача ввести слово,
в якому є буква "о" (враховуються як великі так і маленькі). 
Цикл не повинен завершитися, якщо  користувач ввів слово без букви "о".'''


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
        break

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


'''2. Є list з даними 
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який сформує новий list (наприклад lst2), 
який містить лише змінні типу стрінг, які присутні в lst1. 
Зауважте, що lst1 не є статичним і може формуватися динамічно від запуску до запуску.'''

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []

for item in lst1:
    if isinstance(item, str):
        lst2.append(item)

print('В списку lst1 містяться натсупні елементи типу стрінг:', lst2)

'''3 Є стрінг з певним текстом (можна скористатися input або константою). 
Напишіть код, який визначить кількість слів в цьому тексті, 
які закінчуються на "о" (враховуються як великі так і маленькі).'''

input_text = input('Введіть будь-який текст: ')

world_list = input_text.split()
len_world_list_endswith_о = []

for world in world_list:
    if world.lower().endswith('о'):
        len_world_list_endswith_о.append(world)

list_len = len(len_world_list_endswith_о)
if list_len%10 == 1:
    worlds = 'слово'
elif 1 < list_len%10 < 5:
    worlds='слова'
else:
    worlds='слів'

print(f'В введеному тексті {list_len} {worlds}, які закінчуються на "о"')
