# Алексей Головлев, группа БСБО-07-19

heap = int(input())
f = False
while heap != 0:
    if heap > 5 and heap != 8:
        heap -= 3
    elif heap == 5:
        heap -= 1
    elif heap == 4:
        heap -= 3
    elif heap == 3 or heap == 8:
        heap -= 2
    elif heap == 2:
        heap -= 1
    else:
        print('ход машины ', heap)
        f = True
        break
print('ход машины ', heap)
rocks = 500
while rocks > heap and 3 < rocks:
    rocks = int(input())
    heap -= rocks
    print('ваш ход ', heap)
    if f:
        print('Ты победил')
    else:
        print('ИСКИН победил')