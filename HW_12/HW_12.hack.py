import string
import random
import zipfile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем и возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False


def generate_password():
    password = ''
    chars = '0123456789'
    for i in range(PASSWORD_LENGTH):
        password += random.choice(random.choice(chars))
    return password


def hack_archive(file_name):
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    while True:

        password = generate_password()
        if password in wrong_passwords:
            continue
        elif extract_archive(file_to_open, password):
            break
        wrong_passwords.append(password)
        tries += 1

    print(f'Archive {file_name} is hacked. Password - {password}')
    print(f'Password was found after {tries} tries')


#############
filename = 'task.zip'
hack_archive(filename)


# #2.
# Реализовать тип, который будет вести себя на запись как словарь, а на чтение как списоk

# 1)txt

dog = dict(name="Gucci", age=5, weight=5.5)

try:
    with open('dog.txt', 'w') as file:
        for key, val in dog.items():
            file.write('{}:{}\n'.format(key, val))
    with open('dog.txt', 'r') as file:
        print(file.read())

except Exception as e:
    print("Ошибка при работе с файлом:", e)

# 2)json - обратное преобразование как-то не очень))

# import json
#
# dog = {
#     "name": "Gucci",
#     "age": 5,
#     "weight": 5.5
# }
#
# with open('dog.json', "w") as file:
#     json.dump(dog, file, indent=4)
#
# with open('dog.json', 'r') as file:
#     data = json.load(file)
#     data_list = data.items()
#     print(data_list)
