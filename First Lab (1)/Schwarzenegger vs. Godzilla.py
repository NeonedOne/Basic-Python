# Алексей Головлев, группа БСБО-07-19

j, k = 0, 1

for i in range(int(input())):
    a, b = int(input()), int(input())
    j = j * b + a * k
    k *= b

x, y = j, k

while y > 0:
    x, y = y, x % y

print(j // x, '/', k // x, sep="")
