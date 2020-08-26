# Напишите программу, которая выводит все кратные пяти(5) числа, между двумя, которые введет пользователь.



print('Введите два целых числа через пробел:')
num1, num2 = input().split()
num1 = int(num1)
num2 = int(num2)
print('Кратные пяти числа между ними: ')
i = num1
# while i <= num2:
#     if i % 5 == 0:
#         print(i)
#     i = i + 1

for i in range(num1, num2 + 1):
    if i % 5 == 0:
        print(i)