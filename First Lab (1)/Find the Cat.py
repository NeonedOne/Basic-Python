# Алексей Головлев, группа БСБО-07-19

num_of_strings = int(input())
check_if_true = False

while num_of_strings > 0:
    string = input()
    if "Кот" in string or "кот" in string:
        check_if_true = True
    num_of_strings -= 1
if check_if_true:
    print("МЯУ")
