# Алексей Головлев, группа БСБО-07-19

first_player = int(input())
second_player = int(input())

num_of_stack = 0
how_much_taken = 0

while True:
    num_of_stack = int(input())
    how_much_taken = int(input())

    if num_of_stack == 1:
        if first_player - how_much_taken >= 0:
            first_player -= how_much_taken
    else:
        if second_player - how_much_taken >= 0:
            second_player -= how_much_taken
    if first_player <= 0:
        first_player = 0
    elif second_player <= 0:
        second_player = 0
    print(first_player, second_player)
    if first_player == 0 and second_player == 0:
        break
