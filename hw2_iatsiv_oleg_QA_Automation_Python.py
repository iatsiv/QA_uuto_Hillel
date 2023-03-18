'''1 Сформуйте стрінг, в якому міститься інформація про певне слово.
"Word [тут слово] has [тут довжина слова, отримайте з самого сдлва] letters", наприклад "Word 'Python' has 6 letters".
Для отримання слова для аналізу скористайтеся константою або функцією input().'''

input_word = input('Enter a word to find out its length: ')

if input_word.isalpha():
    letter_counter = f'Word \"{input_word}\" has {len(input_word)} letters'
    print(letter_counter)
elif input_word.isdigit():
    print(f'\"{input_word}\" isn\'t a word, it\'s digit. Try again :( ')
else:
    print(f'\"{input_word}\" isn\'t a word. The entered value doesn\'t contain only letters. Try again :( ')


'''2. Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік (можно використати константу або функцію input(), 
на екран має бути виведено лише одне повідомлення, також подумайте над варіантами, коли введені невірні дані).
якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!" '''

clients_age = input('Введіть, будь-ласка, свій вік: ')

if clients_age.isdigit():
    clients_age = int(clients_age)
    if str(clients_age).find('7') != -1:
        print("Вам сьогодні пощастить")
    elif 7 > clients_age > 0:
        print("Де твої батьки?")
    elif 16 > clients_age >= 7:
        print("Це фільм для дорослих!")
    elif 16 > clients_age >= 7:
        print("Це фільм для дорослих!")
    elif 123 > clients_age > 65: # вік 122 найстаршої людина на планеті
        print("Покажіть пенсійне посвідчення!")
    elif clients_age >= 123:
        print("Люди стільки не живуть!")
    else:
        print("А білетів вже немає!")
else:
    print(f'\"{clients_age}\" не схоже на вік, введіть ваш вік, будь-ласка :) ')