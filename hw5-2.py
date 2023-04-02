
''' 1. створити АРІ на базі гугл таблиці, містить поля "назва товару",
"опис товару", "ціна" (інтова чи флоат), "залишок" (інтовий чи флоат),
"містить глютен" (булеве тру чи фолс (виставляєте прапорцем).
заповнити мінімум 10 позицій. дані мають бути отримати по зовнішньому ключу "goods" (not "data")'''

my_url = 'https://script.google.com/macros/s/AKfycbxjG4w4F4EHBNY2B_PR6Yl_HcH7kI6lQWwiGe-PoPSd2j0qrPen9R4kUuS_Asj7UBv7/exec'
print("Завдання 6.1")
print("Лінка з даними:", my_url)

'''2. за допомогою requests завантажити створені дані.
порахувати вартість всіх товарів та товарів без глютена.
ну і requirements.txt прикріпіть'''

import requests


url = 'https://script.google.com/macros/s/AKfycbxjG4w4F4EHBNY2B_PR6Yl_HcH7kI6lQWwiGe-PoPSd2j0qrPen9R4kUuS_Asj7UBv7/exec'
response = requests.get(url)
goods = response.json()
products = goods['goods']

sum_price_gluten_free = 0
sum_price = 0

for product in products:
    product_price = product['price']
    sum_price += product_price

    if product['hasGluten'] is False:
        sum_price_gluten_free += product_price

print("Завдання 6.2")
print(f"Сума всіх товарів: {sum_price}")
print(f"Сума всіх товарів без глютену: {sum_price_gluten_free}")
