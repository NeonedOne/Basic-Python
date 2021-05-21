num = 0
first_pile = int(input())
second_pile = int(input())
if first_pile > second_pile:
    print("Искин отобрал", first_pile - second_pile)
    first_pile = first_pile - (first_pile - second_pile)
    print("Осталось в куче :", first_pile, second_pile)
elif first_pile < second_pile:
    print("Искин отобрал", second_pile - first_pile)
    second_pile = second_pile - (second_pile - first_pile)
    print("Осталось в куче:", first_pile, second_pile)
else:
    print("Искин отобрал")
    first_pile -= 1
    print("Осталось:", first_pile, second_pile)
while first_pile + second_pile != 0:
    choose_of_player_1 = int(
        input("Введите из какой кучки вы заберёте камни, 1 или 2: "))
    while choose_of_player_1 != 2 and choose_of_player_1 != 1:
        choose_of_player_1 = int(input("Введите из какой кучки взять камни,\
1 или 2: "))
    choose_of_player_2 = int(input("Введите сколько камней взятье: "))
    if choose_of_player_1 == 2:
        while choose_of_player_2 > second_pile:
            print("Введите сколько камней взять")
            choose_of_player_2 = int(input())
    elif (choose_of_player_1 == 1):
        while choose_of_player_2 > first_pile:
            choose_of_player_2 = int(input("Введите сколько камней взять: "))
    if choose_of_player_1 == 2:
        num
        second_pile = second_pile - choose_of_player_2
        print(first_pile, second_pile)