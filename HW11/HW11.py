"""
ITEMS       3       2       2 + XXX
------------------------------------
XXX         100     10      100
A           90      9       18
B           80      8       16
C           70      7       14
D           60      6       12
E           50      5       10
F           40      4       8
G           30      3       6
H           20      2       4
I           10      1       2
"""


"""
Суть задачи:
юзер пришел в казино, сел за автомат, начал игру и у него начали выпадать рандомно величины из представленных выше.
Нужно написать впрограмму, которая за каждым вводом "Играть" (на Ваше усмотрение) - делал вывод полученых очков в комбинации и количество очков 
юзера за всю игру. Если юзре ввел "Выйти" (на ваше усмотрение) - выходит из программы и показвает количество очков за игру.
Выше есть таблица со значениями сколько какая комбинация весит.
"""
# wheel1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
# wheel2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
# wheel3 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]

import random

wheel1_dict = {"A": 18, "B": 16, "C": 14, "D": 12, "E": 10, "F": 8, "G": 6, "H": 4, "I": 2, "XXX": 100}
wheel2_dict = {"A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 4, "G": 3, "H": 2, "I": 1, "XXX": 10}
wheel3_dict = {"A": 90, "B": 80, "C": 70, "D": 60, "E": 50, "F": 40, "G": 30, "H": 20, "I": 10, "XXX": 100}

wheel = [wheel1_dict, wheel2_dict, wheel3_dict]


def choiceWheel():
    wheel_number = random.choice(wheel)
    # return wheel_number
    wheel_number_dict = wheel_number
    return wheel_number_dict


def choiceWin():
    win = random.choice(list(choiceWheel().values()))
    return win


def main():
    count = 0
    while True:

        choice = input('Do you want to play? y/n\n')
        choice = choice.lower()

        if choice == 'y':
            choiceWheel()

            current = choiceWin()
            print('You win is ' + str(current))
            count += current
        elif choice == 'n':
            print('Congratulacions! Your total win is ' + str(count))
            break
        else:
            print('Wrong letter')
    print('See you!')


if __name__ == '__main__':
    main()
