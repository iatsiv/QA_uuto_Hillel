'''2. Візьміть функції з попереднього ДЗ, покладіть їх у файл lib.py
і імпортуйте в основний файл для виконання'''

from lib import stupid_calc
from lib import what_season

my_data = '2.2'
num_1 = 7
num_2 = 8
operation = '*'

what_season_in_data = what_season(my_data)
stupid_calc = stupid_calc(num_1, num_2, operation)

print(what_season_in_data)
print(stupid_calc)