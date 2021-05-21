# Алексей Головлев, группа БСБО-07-19

matrix = []
height, width = int(input()), int(input())

for i in range(height):
    matrix.append(input())
result=[]
for i in matrix[::2]:
    result.append(i[::2])
height = height // 2
width = width // 2
print(height, width)
for i in result:
    print(i)