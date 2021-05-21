# Алексей Головлев, группа БСБО-07-19

counter = 0
first_bro_res = [int(input()) for i in range(int(input()))]
second_bro_res = first_bro_res.copy()
for i in range(int(input())):
    if int(input()) == 1:
        first_bro_res[int(input())] += int(input())
    else:
        second_bro_res[int(input())] += int(input())
for i in range(len(first_bro_res)):
    counter += int(first_bro_res[i] == second_bro_res[i])
print(*first_bro_res)
print(*second_bro_res)
print(counter)