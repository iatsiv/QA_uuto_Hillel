'''1. Задача: Створіть дві змінні first=10, second=30.
Виведіть на екран результат математичної взаємодії (+, -, *, / и тд.)
 для цих чисел.'''

first = 10
second = 30

print('перше число:', first)
print('друге число:', second)

sum = first + second
print('сума чисел:',sum)

difference = first - second
print('різниця першого і другого числа:',difference)

multiply = first * second
print('добуток чисел:',multiply)

division = first / second
print('ділення першого на друге число:',division)

division_rounding = first // second
print('ділення першого на друге число з округленням вниз:',division_rounding)

exponentiation = first ** second
print('перше число в ступені другого:',exponentiation)

remainder = first % second
print('остача від ділення першого на друге число:',remainder)


'''2. Задача: Створіть змінну и по черзі запишіть в неї 
результат порівняння (<, > , ==, !=) чисел з завдання 1. 
 Виведіть на екран результат кожного порівняння.'''

comparison = first < second
print('перше число менше другого:', comparison)

comparison = first > second
print('перше число більше другого:', comparison)

comparison = first == second
print('перше число рівно другому:', comparison)

comparison = first != second
print('перше число не рівно другому:', comparison)


'''3. Задача: Створіть змінну - резкльтат 
конкатенації строк "Hello " та "world!".'''

string_1 = "Hello "
string_2 = "world!"

result = string_1 + string_2
print('Завдання 3:',result)