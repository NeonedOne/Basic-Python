# Алексей Головлев, группа БСБО-07-19

def transpose(matrix):
    return [list(x) for x in zip(*matrix)]


matrix = [[1]]
transpose(matrix)
for line in matrix:
    print(*line)
print()

matrix = [[1, 2], [3, 4]]
transpose(matrix)
for line in matrix:
    print(*line)
