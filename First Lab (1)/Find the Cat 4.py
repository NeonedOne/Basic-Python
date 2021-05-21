# Алексей Головлев, группа БСБО-07-19

num_of_strings = int(input("Кол-во строк: "))
is_cat_found = False

for i in range(num_of_strings):
    string = input()

    if " кот " in string.replace(".", " ").replace(",", " ") or " Кот " in string.replace(".", " ").replace(",", " "):
        is_cat_found = True
    if " пёс " in string.replace(".", " ").replace(",", " ") or " Пёс " in string.replace(".", " ").replace(",", " "):
        is_cat_found = False

if is_cat_found:
    print("МЯУ")
else:
    print("НЕТ")
