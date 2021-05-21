# Алексей Головлев, группа БСБО-07-19

total = input().split(" ")
correct_calculations = 0
wrong_calculations = []

for i in range(int(total[0])):
    goods = input().replace(" ", "").replace("=", "*").split("*")
    correct_calculations += int(goods[0]) * int(goods[1])
    if int(goods[0]) * int(goods[1]) != int(goods[2]):
        wrong_calculations.append(i+1)
print(int(total[-1]) - correct_calculations)
print(*wrong_calculations)