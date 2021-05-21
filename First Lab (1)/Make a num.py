# Алексей Головлев, группа БСБО-07-19

code = int(input())
num1 = code // 100
num2 = code % 100 // 10
num3 = code % 10
modified_num1 = str(num1 + num2)
modified_num2 = str(num2 + num3)
if num2 + num3 >= num1 + num2:
    print(modified_num2 + modified_num1)
else:
    print(modified_num1 + modified_num2)
