'''є url https://dummyjson.com/users (100 сторінок)
вивести в консоль середній вік чоловіків з Brown волоссям,
а також сформувати список людей, що проживають в місті Louisville
обовязково прикріпити requirements.txt'''

import requests


url = 'https://dummyjson.com/users?limit=100'
response = requests.get(url)
our_users = response.json()
users = our_users['users']

avg_age = 0
sum_age = 0
count = 0
list_dwellers_in_city = []

for user in users:
    user_age = user['age']
    gender = user.get('gender', '')
    hairs = user['hair']
    hair_colour = hairs['color']
    dweller = (user['firstName'], user['lastName'])
    address = user['address']
    citys = address.get('city', '')
    citys2 = address.get('city', '')

    if hair_colour.lower() == 'brown' and gender.lower() == 'male':
        sum_age += user_age
        count += 1
        print(f'{count}, {user_age}')
    if citys.lower() == 'louisville':
        list_dwellers_in_city.append(dweller)

avg_age = sum_age/count

print(f"Середній вік всіх {count} коричневоволосих чоловіків складає", round(avg_age))
print("В місті Louisville проживають наступні люди:")

count = 0
for dweller in list_dwellers_in_city:
    count += 1
    print(f"{count}. {dweller[0]} {dweller[1]}")
