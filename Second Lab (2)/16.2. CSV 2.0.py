# Алексей Головлев, группа БСБО-07-19

data = [list(input().replace(".", ",").split(",")) for i in range(int(input()))]
for i in range(int(input())):
    coordinates = list(input().split(","))
    print(data[int(coordinates[0])][int(coordinates[1])])
