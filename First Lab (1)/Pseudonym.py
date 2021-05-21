# Алексей Головлев, группа БСБО-07-19

num_of_stones = int(input())

while num_of_stones > 0:
    num_1 = num_of_stones % 4
    if num_1 == 0:
        num_1 = 2
    num_of_stones -=num_1
    print(num_1, num_of_stones)
    if num_1 == num_of_stones:
        print('Comp has won')
    else:
        num_1 = 0
        num_1 = int(input())
        if 1 <= num_1 <= 3 and num_1 <= num_of_stones:
            continue
        else:
            while not(1 <= num_1 <= 3 and num_1 <= num_of_stones):
                print('error', num_1)
                num_1 = (input())
    num_of_stones -= num_1
    print(num_1, num_of_stones)
    if num_of_stones == 0:
        print('you won')