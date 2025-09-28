while True:
    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        op = input("Введите операцию (+, -, , /) или 0 для выхода: ")

        if op == "0":
            print("Выход из программы...")
            break
        elif op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "":
            print(num1 * num2)
        elif op == "/":
            if num2 == 0:
                print("Ошибка: деление на ноль невозможно!")
            else:
                print(num1 / num2)
        else:
            print("Неизвестная операция")

    except ValueError:
        print("Ошибка: введите корректное число!")

    print("\n---\n")