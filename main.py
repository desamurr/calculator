num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
op = input("Введите операцию (+, -, , /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Неизвестная операция")