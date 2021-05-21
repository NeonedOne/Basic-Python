# Алексей Головлев, группа БСБО-07-19

axis_x = int(input())
axis_y = int(input())
side_of_the_world = input()
num = int(input())
flag = True
x = 0
y = 0
k = 0
while side_of_the_world != 'стоп':
    if axis_x == x and axis_y == y:
        flag = False
    if side_of_the_world == 'север':
        y += num
        if flag:
            k += 1
    elif side_of_the_world == 'юг':
        y -= num
        if flag:
            k += 1
    elif side_of_the_world == 'запад':
        x -= num
        if flag:
            k += 1
    elif side_of_the_world == 'восток':
        x += num
        if flag:
            k += 1
    side_of_the_world = input()
    if side_of_the_world != 'стоп':
        num = int(input())
print(k)
