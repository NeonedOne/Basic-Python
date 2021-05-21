# Алексей Головлев, группа БСБО-07-19

n = int(input())
s = [[]]

for i in range(n - 1):
    s.append([int(j) for j in input().split()])

point = input().split()
a, a_1 = int(point[0]), int(point[1])

p = s[max(a, a_1)][min(a, a_1)]
b = -1

for i in range(n):
    if i != a and i != a_1:
        if p > s[max(i, a_1)][min(i, a_1)] + s[max(a, i)][min(a, i)]:
            p = s[max(i, a_1)][min(i, a_1)] + s[max(i, a_1)][min(i, a_1)]
            b = i
if b != -1:
    print(b)
else:
    print(a)