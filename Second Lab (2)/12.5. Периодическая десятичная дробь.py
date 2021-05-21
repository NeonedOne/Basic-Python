# Алексей Головлев, группа БСБО-07-19

number = int(input())
r = 1
rr = []
dd = []
while r not in rr:
    rr.append(r)
    dd.append(10 * r // number)
    r = 10 * r % number

print(*dd[rr.index(r):], sep='')
