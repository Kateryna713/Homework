#   Создать файл, в нем написать текст.
#     Считать данные с файла и вывести в консоль
#     Считать данные с этого же файла и записать в новый файл
#     Считать данные с этого же файла, преобразовать (любые операции) и записать в этот же файл без

with open('test.txt', 'w') as file:
     file.write('Test file for homework_8.')

# 1)
with open('test.txt', 'r') as file:
    print(file.read())

# 2)
with open('test.txt', 'r') as file, open ('test_1.txt','w') as file2:
    info = file.read()
    file2.write(info)

# 3)
with open('test.txt', 'r+') as file:
     data = file.read()
     file.write ('\nJust for test')
with open('test.txt', 'r') as file:
     print(file.read())

# with open('test.txt', 'a+') as file:
#     file.write('\nJust for test')
#     file.seek(0) - Вопрос, возвращение на нач.позицию в данном случае эквивалентно перезапуску "with open('test.txt', 'r') as file:"?
#     print(file.read())







