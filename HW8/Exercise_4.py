# Сохраним последний успешный запуск
# Нужно записать в json файл данные о последней удачной попытке угадать число из задачи 3.
# В файле должны быть:
#  - число
#  - номер попытки
#  - дата записи в файл (можно посмотреть такое в cw.py)



import json
from datetime import datetime
from random import random

n = round(random() * 50)
i = 1
print('You have 10 tries to guess the number.')
while i <= 10:
    try:
        chance = int(input("Chance " + str(i) + ":"))
        if chance == n:
            print('Congrats! You guess it!')
            data = {
                'number': n,
                'attemp': i,
                'time':str(datetime.now())
            }
            with open('random_victory.json', 'w') as file:
                json.dump(data, file, indent=4)
                print(data)

            break
        else:
            print('Try again!')
            i += 1
    except(TypeError, ValueError):
        print("Неправильный ввод. Попробуйте еще раз...")
        continue
else:
    print("No more chances. Unknown number was", n)

