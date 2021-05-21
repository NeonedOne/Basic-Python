# Алексей Головлев, группа БСБО-07-19

list_string, index = input(), int(input()) - 1
if index < 0 or index >= len(list_string):
    print("Ошибка")
else:
    print(list_string[index])
