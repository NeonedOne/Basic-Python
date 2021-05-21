#Алексей Головлев, группа БСБО-07-19

code = int(input())
num1 = code // 100
num2 = code  % 100 // 10
num3 = code % 10
if num1 == num2 == num3:
    print('В числе числе все цифры одинаковые')
elif (num1 == num2) or (num2 == num3) or (num1 == num3):
    print('В числе две одинаковые цифры')
else:
    print("ОК")
