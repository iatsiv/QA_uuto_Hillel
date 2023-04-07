'''1. Напишіть функцію, яка приймає два аргументи.
а. Якщо обидва аргумени відносяться до числових типів
функція пермножує ці аргументи і повертає результат
b. Якшо обидва аргументи відносяться до типу стрінг
функція обʼєднує їх в один і повертає
c. В будь-якому іншому випадку - функція повертає кортеж
з двох агрументів'''



data1 = False
data2 = True

def fun_math(data1, data2):
    if isinstance(data1, (int, bool)) and isinstance(data2, (int, bool)):
        result = (data1, data2)
    elif isinstance(data1, (int, float)) and isinstance(data2, (int, float)):
        result = data1 * data2
    elif isinstance(data1, str) and isinstance(data2, str):
        result = data1 + data2
    else:
        result = (data1, data2)
    return result


print(fun_math(data1, data2))

'''2. Візьміть код з заняття і доопрацюйте натупним чином:
a. користувач має вгадати чиcло за певну кількість спроб. 
користувач на початку програми визначає кількість спроб
b. додайте підказки. якщо рвзнися між числами 
більше 10 - "холодно", від 10 до 5 - "тепло", 1-4 - "гаряче"
'''

from random import randint


def get_count_attempts():

    while True:
        try:
            return int(input('Enter the number of attempts (int): '))
        except ValueError:
            print('Number please 👿!')


def get_ai_number():
    number = randint(1, 10)
    return number


def get_user_number():

    while True:
        try:
            return int(input('Enter the number (int): '))
        except ValueError:
            print('Number please!')


def check_numbers(ai_number, user_number):
    if user_number == 777:
        print('You are cheater!')
        return True
    difference = abs(ai_number - user_number)
    if difference > 10:
        print('Cold🥶')
    elif difference >= 5:
        print('Warm🥴')
    elif difference > 0:
        print('Hot🥵')
    result = ai_number == user_number
    return result


def game_guess_number():
    print('Game begins!')

    ai_number = get_ai_number()
    count_attempts = get_count_attempts()
    print("Let`s GO!")

    while True:
        user_number = get_user_number()
        is_game_end = check_numbers(ai_number, user_number)
        count_attempts -= 1

        if is_game_end:
            print('User win 🥳 ')
            break
        elif count_attempts == 0:
            print('GAME OVER! See you soon (x . x) ~~zzZ!')
            break
        else:
            print('Wrong!!!  (╯°益°)╯彡┻━┻ ')
            print(f'But, you have {count_attempts} attempts left...')
            print('Let`s try again!')


game_guess_number()
