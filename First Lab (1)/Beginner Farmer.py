cash = int(input())
heads = int(input())
for i in range(1, 1 + cash // 20):
    for j in range(1 + (cash - i * 20) // 10):
        t = heads - (i + j)
        if i * 20 + j * 10 + t * 5 == cash:
            print(i, j, t)