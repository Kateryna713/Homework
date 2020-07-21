''''
1. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время
года, которому этот месяц принадлежит (зима, весна, лето или осень).
'''


# def get_season(number):
#     # write your code here
print ("Задание 1.")
number = int(input("Input number from 1 to 12: "))
            # Var 1

def get_season(number):
    i = number
    if i == 1 or i == 2 or i == 12:
        return ('It is winter')
    elif i == 3 or i == 4 or i == 5:
        return ("It is spring")
    elif i == 6 or i == 7 or i == 8:
        return ('It is summer')
    elif i == 9 or i == 10 or i == 11:
        return ('It is autumn')


print(get_season(number))

#             Var2
def get_season(number):
    if number in (12, 1, 2):
        return 'It is winter'
    elif number in (3, 4, 5):
        return 'It is spring'
    elif number in (6, 7, 8):
        return 'It is summer'
    elif number in (9, 10, 11):
        return 'It is autumn'

print(get_season(number))
"""
2. Реализовать функцию, которая принимает строку и расделитель и возвращает словарь {слово: количество повторений}
"""
#                Var1
print()
print ("Задание 2.")

from collections import Counter


def converter(string, delimeter):
    return Counter(string.split(delimeter))

my_str = input("Please enter your string: ")
my_str = my_str.lower()
delimiter = input("Please enter what will be delimiter: ")

print(converter(my_str, delimiter))

#                Var2
#
def converter(my_str, delimeter):
    list_converter = my_str.split(delimeter)
    my_dict = {}
    for e in list_converter:
        if e in my_dict:
            my_dict[e] = my_dict[e] + 1
        else:
            my_dict[e] = 1
    return (my_dict)


print(converter(my_str, delimiter))

#              Var 3

def converter(my_str, delimeter):
    list_converter = my_str.split(delimeter)
    my_dict = {}
    for e in list_converter:
        my_dict[e] = my_dict.get(e, 0) + 1
    return (my_dict)


print(converter(my_str, delimiter))

#               Var 4


def converter(my_str, delimeter):
    list_converter = my_str.split(delimeter)
    my_dict = {}
    for e in list_converter:
        my_dict[e] = list_converter.count(e)
    return (my_dict)


print(converter(my_str, delimiter))





'''
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, 
площадь квадрата и диагональ квадрата.
'''

import math

def get_square_data(a):
    p = a*4
    s = a**2
    d = (2*a**2)**.5
    # d = math.sqrt(2)*a или так)
    return p,s,d
    # d = math.sqrt(2)*a

a =  float(input("Введите сторону квадрата: "))

print(get_square_data(a))
