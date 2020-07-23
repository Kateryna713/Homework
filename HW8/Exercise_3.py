#  Угадай число
# Рандомное число можно сделать через модуль random
# Диапазон 1 - 50
# Попыток 10 (можно менять)
# Рандомите число из диапазона,
# запрашиваете число у юзера, валидируя его,
# сравниваете, если угадал - завершаеться программа,
# ксли нет снова спрашиваете число.
# Если юзер не вложился в количество попыток - завершаеете ее с сообщением что попыток больше нет

from random import random

n = round(random() * 50)
i = 1
print('You have 10 tries to guess the number.')
while i <= 10:
    try:
        chance = int(input("Chance " + str(i) + ":"))
        if chance == n:
            print('Congrats! You guess it!')
            break
        else:
            print('Try again!')
            i += 1
    except(TypeError, ValueError):
        print("Неправильный ввод. Попробуйте еще раз...")
        continue
else:
    print("No more chances. Unknown number was", n)
