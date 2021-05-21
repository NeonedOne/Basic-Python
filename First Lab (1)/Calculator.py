#Алексей Головлев, группа БСБО-07-19

num1 = float(input())
num2 = float(input())
operation = input()

if operation == '+':
    print(num1 + num2)
elif operation == '-':
    print(num1 - num2)
elif operation == '/':
    if num2 == 0:
        print('888888')
    else:
        print(num1 / num2)
elif operation == '*':
    print(num1 * num2)
else:
    print('888888')
