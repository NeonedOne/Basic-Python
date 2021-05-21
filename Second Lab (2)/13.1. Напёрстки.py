# Алексей Головлев, группа БСБО-07-19

object_list = []
for i in range(int(input())):
    object_list.append(input())
for i in range(int(input())):
    change_list = [object_list[int(input())-1] for j in range(int(input()))]
    object_list = change_list
print(*object_list, sep="\n")
