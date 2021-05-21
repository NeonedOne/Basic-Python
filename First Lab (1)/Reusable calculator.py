# Алексей Головлев, группа БСБО-07-19

firstnum = int(input("первое число:"))
operation = input("операция:")

while operation != "x":
    if operation == "+":
        secondnum = int(input("второе число:"))
        firstnum = (firstnum + secondnum)
        print(firstnum)
        print()
    elif operation == "-":
        secondnum = int(input("второе число:"))
        firstnum = (firstnum - secondnum)
        print(firstnum)
        print()
    elif operation == "*":
        secondnum = int(input("второе число:"))
        firstnum = (firstnum * secondnum)
        print(firstnum)
        print()
    elif operation == "/":
        secondnum = int(input("второе число:"))
        if secondnum != 0:
            firstnum = (firstnum / secondnum)
            print(firstnum)
            print()
        else:
            print()
    elif operation == "%":
        secondnum = int(input("второе число:"))
        firstnum = (firstnum % secondnum)
        print(firstnum)
        print()
    elif operation == "!":
        if firstnum > 0:
            factorial = 1
            while firstnum > 1:
                factorial *= firstnum
                firstnum -= 1
            print(factorial)
            firstnum = factorial
            print()
        else:
            print()
    else:
        print("Ошибка,повторите ввод")
    firstnum = int(input("первое число:"))
    operation = input("операция:")
if operation == "x":
    print(firstnum)
