import div
import add
import mult
import sub



def main():

    while True:

        try:
            var_a = input('Введите первое число: ')
            if var_a == "exit":
                print ('Выход')
                exit()
            else:
                var_a = float(var_a)
                pass

            var_c = input("Введите знак операции (+,-,*,/): ")

            if var_c in ('+', '-', '*', '/'):
                pass
            else:
                print("Неправильный знак. Попробуйте еще раз...")
                continue

            var_b = float(input('Введите второе число: '))

        except(TypeError, ValueError):
            print ("Неправильный ввод. Попробуйте еще раз...")
            continue
        break

    if var_c == "/":
        count = div.div(var_a, var_b)

    elif var_c == "*":
        count = mult.mult(var_a, var_b)
    elif var_c == "+":
        count = add.add(var_a, var_b)
    elif var_c == '-':
        count = sub.sub(var_a,var_b)
    print("Результат равен  "+ str(count))


if __name__ == '__main__':
    main()




