# Алексей Головлев, группа БСБО-07-19

list_of_all_dishes = []

m = int(input())
for i in range(m):
    list_of_all_dishes.append(input())

n = int(input())
for i in range(n):
    num_of_dished = int(input())
    for j in range(num_of_dished):
        name_of_dish = input()
        if name_of_dish in list_of_all_dishes:
            list_of_all_dishes.remove(name_of_dish)

print(*list_of_all_dishes, sep="\n")
