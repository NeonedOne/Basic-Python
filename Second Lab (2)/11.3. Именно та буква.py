# Алексей Головлев, группа БСБО-07-19

text, fav_num, fav_char = input(), input(), input()
try:
    fav_num = int(fav_num) - 1
    if len(fav_char) > 1 or fav_num < 0:
        print("Ошибка")
    elif fav_char == text[fav_num]:
        print("Да")
    else:
        print("Нет")
except ValueError or IndexError:
    print("Ошибка")
