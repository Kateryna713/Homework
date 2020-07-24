# Написать игру. 2 игрока бросают игровые кубики по 10 раз,
# нужно определить кто выиграл и вывести результаты обоих игроков (суммы бросков).
# Если у двух игроков за 1 ход выпало на кубиках одинаковое число, то игроки перебрасывают кубики.

"""

"""
import random

def dice_roll():
    while True:
        player1_total = 0
        player2_total = 0
        i=1
        while i <= 10:
            player1_number  = random.randint(1, 6)
            player2_number = random.randint(1, 6)
            if player1_number == player2_number:
                continue
            else:
                player1_total = player1_number + player1_total
                player2_total = player2_number + player2_total
                i+=1
        print ("Player 1 total sum = " + str(player1_total))
        print ("Player 2 total sum = " + str(player2_total))
        break
    if player1_total > player2_total:
        print('Player 1 win! Congratulations!!!')
    elif player1_total < player2_total:
        print('Player 2 win! Congratulations!!!')
    else:
        print ('It is a drow! Friendship wins!')


def main():
    y_n = input('Играем?[yes/no]')
    if y_n == 'yes':
        dice_roll()
    else:
        print('Exit')

if __name__ == '__main__':
    main()