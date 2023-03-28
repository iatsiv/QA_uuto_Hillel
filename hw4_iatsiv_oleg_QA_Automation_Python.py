

'''1. Є list довільних чисел,
наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44].
Напишіть код, який видалить (не створить новий, а саме видалить!)
 з нього всі числа, які менше 21 і більше 74.'''

random_lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

for list_elmt in range(len(random_lst)-1,-1,-1):
    if 21 > random_lst[list_elmt] or random_lst[list_elmt] > 74:
            random_lst.pop(list_elmt)

print('Відфільтрований список без чисел менше 21 і більше 74: ', random_lst)

while True:
    removed = False  # флаг, що вказує, чи було видалено хоча б один елемент
    for i in range(len(lst)-1, -1, -1):
        if lst[i] < 21 or lst[i] > 74:
            del lst[i]
            removed = True  # встановлюємо флаг, що елемент було видалено
    if not removed:
        break  # якщо не було видалено жодного елемента, виходимо з циклу while

print(lst)

while i < n:
    if lst[i] < 21 or lst[i] > 74:
        del lst[i]
        n -= 1  # зменшуємо довжину списку на 1
    else:
        i += 1  # збільшуємо лічильник ітерацій на 1

print(lst)

lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

'''2. Є два довільних числа які відповідають за мінімальну 
і максимальну ціну. Є Dict з назвами магазинів і цінами: 
{ "citos": 47.999, "BB_studio" 42.999, "mo-no": 49.999, "my-main-service": 37.245, 
"buy-now": 38.324, "x-store": 37.166, "the-partner": 38.988, "store-123": 37.720, 
"roze-tka": 38.003}. 
Напишіть код, який знайде і виведе на екран назви магазинів, 
ціни яких потрапляють в діапазон між мінімальною і максимальною ціною.
Наприклад:
lower_limit = 35.9
upper_limit = 37.339
> match: "x-store", "main-service"'''

lower_limit = 48.0
upper_limit = 50.0
shop_list = []

shops_prices = {"citos": 47.999, "BB_studio": 42.999, "mo-no": 49.999,
"my-main-service": 37.245, "buy-now": 38.324, "x-store": 37.166,
"the-partner": 38.988, "store-123": 37.720, "roze-tka": 38.003}

for shop, price in shops_prices.items():
    if lower_limit < price < upper_limit:
        shop_list.append(shop)

print('В заданий діапазон потрапили наступні магазини :', shop_list)
