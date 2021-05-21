# Алексей Головлев, группа БСБО-07-19

heap1 = int(input())
heap2 = int(input())
heap3 = int(input())
while heap1 != 0 or heap2 != 0:
    num = input()
    rocks = int(input())
    if num == '1':
        heap1 -= rocks
    elif num == '2':
        heap2 -= rocks
    else:
        heap3 -= rocks
    print(heap1, heap2, heap3)