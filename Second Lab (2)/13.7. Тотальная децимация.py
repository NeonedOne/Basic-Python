# Алексей Головлев, группа БСБО-07-19

decimation_list = [input() for i in range(int(input()))]
step = int(input())
while decimation_list:
    for name in decimation_list[::step]:
        print(name)
    for name in decimation_list[::step]:
        decimation_list.remove(name)
