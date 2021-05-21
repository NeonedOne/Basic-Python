# Алексей Головлев, группа БСБО-07-19

length = int(input())
width = int(input())

for i in range(1, length + 1):
    for j in range(1, width + 1):
        if len(str(j/i))<=3:
            res = (j/i)
        else:
            res = str(j) + "/" + str(i)
        if i == width+1 or j == length:
            print(str(res))
        else:
            print(res, end=" ")
