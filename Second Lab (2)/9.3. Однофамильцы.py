# Алексей Головлев, группа БСБО-07-19

m = int(input())
list_of_workers = []
list_of_unique_names = []
summator = 0

for i in range(m):
    name = input()
    if name not in list_of_unique_names:
        list_of_unique_names.append(name)
    list_of_workers.append(name)

for i in range(len(list_of_unique_names)):
    if list_of_workers.count(list_of_unique_names[i]) == 1:
        summator += 1
print(summator)