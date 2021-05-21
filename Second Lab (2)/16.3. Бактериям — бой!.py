# Алексей Головлев, группа БСБО-07-19

side_length = int(input())
matrix = [[int(input()) for i in range(side_length)] for j in range(side_length)]

coords = int(input())
for i in range(coords):
    x = int(input())
    y = int(input())
    for y_coord in range(-1, 2):
        for x_coord in range(-1, 2):
            if (0 <= y + y_coord <= side_length - 1) and (0 <= x + x_coord <= side_length - 1):
                if y_coord == 0 and x_coord == 0:
                    if matrix[y + y_coord][x + x_coord] >= 8:
                        matrix[y + y_coord][x + x_coord] -= 8
                    else:
                        matrix[y + y_coord][x + x_coord] = 0
                else:
                    if matrix[y + y_coord][x + x_coord] >= 4:
                        matrix[y + y_coord][x + x_coord] -= 4
                    else:
                        matrix[y + y_coord][x + x_coord] = 0

for y in range(side_length):
    for x in range(side_length):
        print(matrix[y][x], end=" ")
    print("")