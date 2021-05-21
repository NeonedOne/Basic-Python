# Алексей Головлев, группа БСБО-07-19

m = int(input())
n = int(input())
literature_for_summer = []

for i in range(m):
    literature_for_summer.append(input())
for i in range(n):
    if input() in literature_for_summer:
        print("YES")
    else:
        print("NO")
