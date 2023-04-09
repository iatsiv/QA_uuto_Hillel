'''1 Напишіть функцію, яка визначає сезон за датою.
Функція отримує стрінг у форматі "[день].[місяць]"
(наприклад "12.01", "30.08", "1.11" і тд) і повинна
повернути стрінг з відповідним сезоном, до якого
відноситься ця дата ("літо", "осінь", "зима", "весна")'''


def what_season(input_data):
    '''
    Returns the name of the season based on the date
    :param input_day: str in format 'dd.mm'
    :return: str, season
    '''

    try:
        day, month = map(int, input_data.split('.'))
        if day in range(1, 32):
            if month in (12, 1) or (month == 2 and day < 30):
                return 'Winter'
            elif month in (3, 5) or (month == 4 and day < 31):
                return 'Spring'
            elif month in (7, 8) or (month == 6 and day < 31):
                return 'Summer'
            elif month in (9, 11) and day < 31 or month == 10:
                return 'Autumn'
            else:
                return print('The month value is out of range.')
        else:
            return print('The day value is out of range.')
    except:
        print('Invalid date, accepts an arg in str "day.month"')


print(what_season('10.3'))


'''2 Напишіть функцію "Тупий калькулятор", яка приймає 
два числових аргументи і строковий, який відповідає за 
операцію між ними (+ - / *). Функція повинна повертати 
значення відповідної операції (додавання, віднімання, ділення, 
множення), інші операції не допускаються. Якщо функція оримала 
невірний тип данних для операції (не числа) або неприпустимий 
(невідомий) тип операції вона повинна повернути None і вивести 
повідомлення "Невірний тип даних" або "Операція 
не підтримується" відповідно.'''


def stupid_calc(num_1, num_2, operation):
    '''
    Returns multiplication, division, addition or subtraction of two numbers
    :param num_1: numbers
    :param num_2: numbers
    :param operation: str
    :return: int or float
    '''

    if not isinstance(num_1, (int, float)) \
        or not isinstance(num_2, (int, float)) \
        or isinstance(num_1, (bool)) or isinstance(num_2, (bool)):
        print("Невірний тип даних")
        return None
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2
    elif operation == '/':
        if num_2 == 0:
            print("Операція не підтримується")
            return None
        return num_1 / num_2
    elif operation in ('**', '%', '//'):
        print("Операція не підтримується")
        return None
    else:
        return print("Невірний тип даних")


print(stupid_calc(333.3, -0.3333, '/'))
print(stupid_calc(True, False, '*'))