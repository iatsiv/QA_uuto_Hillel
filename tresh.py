#
# import re
# import datetime
#
# def season(date_string):
#     # Перевірка на валідність формату даних
#     if not isinstance(date_string, str) or not date_string or not re.match(r'\d{1,2}\.\d{1,2}', date_string):
#         raise ValueError('Невірний формат даних. Введіть дату у форматі "день.місяць" (наприклад "12.01")')
#
#     # Розділення дати на день і місяць
#     day, month = map(int, date_string.split('.'))
#
#     # Перевірка на валідну дату
#     try:
#         datetime.datetime(year=2023, month=month, day=day)
#     except ValueError:
#         raise ValueError('Невірна дата. Введіть коректну дату.')
#
#     # Визначення сезону за місяцем
#     if month in [12, 1, 2]:
#         return 'зима'
#     elif month in [3, 4, 5]:
#         return 'весна'
#     elif month in [6, 7, 8]:
#         return 'літо'
#     else:
#         return 'осінь'
#
#
# print(season(''))
#
# input_data = '31.9'
#
# a, b = map(int, input_data.split('.'))
#
# print(a)
# print(b)

def calculator(num1, num2, operation):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Невірний тип даних")
        return None
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Ділення на 0 неможливе")
            return None
        return num1 / num2
    else:
        print("Операція не підтримується")
        return None

result = calculator(1,1,'1')
print(result)