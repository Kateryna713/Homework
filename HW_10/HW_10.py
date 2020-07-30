# Ex.1

# Input: Feb 12 2019 2:41PM
# Output: 2019-02-12 14:41:00
# Функция принимает строку (пример - Input) и возвращает строку (пример - Output)


from datetime import datetime



def date_valid():
    while True:
        try:
            year = int(input('Enter a year: '))
            month = int(input('Enter a month: '))
            day = int(input('Enter a day: '))
            hour = int(input('Enter a hour: '))
            minut = int(input('Enter a minuts: '))
            my_date = datetime(year, day, month, hour, minut)
            return my_date

        except(TypeError, ValueError):
            print("Incorrect data format. Try again...")
            continue
        break
# Var/1
# def get_date():
#     my_date_str = date_valid().strftime('%b %d %Y %I:%M%p') # преобразуем объект datetime в строку (наш input)
#     print(my_date_str)
#     date_time_get = datetime.strptime(my_date_str, '%b %d %Y %I:%M%p') # преобразуем строку даты обратно в объект datetime
#     my_date_get_str = datetime.strftime(date_time_get, '"%Y-%m-%d %H.%M.%S"') # преобразуем объект datetime в строку
#     return(my_date_get_str) #наш output

# Var/2,
def get_date():
    my_date_str = date_valid().strftime('%b %d %Y %I:%M%p')
    print(my_date_str)
    return datetime.strptime(my_date_str,'%b %d %Y %I:%M%p').strftime("%Y-%m-%d %H.%M.%S")


print(get_date())









print()
# Ex.2
# Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
# Простое число - это число, которое делится без остатка только на себя и на 1


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Введите число: '))
            print(n)
            if n == 1:
                print("Вы ввели единицу. Она не отнсится ни к простым, ни к составным числам.")
                continue

        except(TypeError, ValueError):
            print("Неправильный ввод. Попробуйте еще раз...")
            continue
        else:
            if is_prime(n) == True:
                print("Число", str(n), "- простое.", sep=' ')
            else:
                print("Число", str(n), "- составное.", sep=' ')
        break


print()
# Напишите функцию, которая принимает 1 аргумент (строка) и выполняет следующие действия на каждую из букв строки:
# i - инкремент (+1)
# d - дикремент (-1)
# s - возведение в квадрат
# o - добавить число в результативный список
# остальные буквы игнорируются
# Исходное число = 0
# Результативный список = []
# Вернуть результативный список
# parse("iiisdoso")  ==>  [8, 64]


def main():
    my_string = input("Provide a string: ")
    my_str_1 = my_string.lower()
    print(my_str_1)
    print(parse(my_str_1))


def parse(my_str_1):
    number = 0
    result_list = []

    for el in my_str_1:
        if el == 'i':
            number = number + 1

        elif el == 'd':
            number = number - 1

        elif el == 's':
            number = number ** 2

        elif el == 'o':
            result_list.append(number)

    return (result_list)


if __name__ == '__main__':
    main()


