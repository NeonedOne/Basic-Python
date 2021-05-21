# Алексей Головлев, группа БСБО-07-19

shopping_list = []

for i in range(int(input())):
    shopping_list.append(input() + " " + input())
print(*reversed(shopping_list), sep="\n")