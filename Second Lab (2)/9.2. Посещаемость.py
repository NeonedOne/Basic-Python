# Алексей Головлев, группа БСБО-07-19

m = int(input())
list_of_students = []
list_of_unique_names = []

for i in range(m):
    n = int(input())
    for j in range(n):
        name = input()
        if name not in list_of_unique_names:
            list_of_unique_names.append(name)
        list_of_students.append(name)

for i in range(len(list_of_unique_names)):
    if list_of_students.count(list_of_unique_names[i]) == m:
        print(list_of_unique_names[i])
