# Алексей Головлев, группа БСБО-07-19

counter = 0
string = "nothing"

while string != "СТОП":
    string = input()
    counter += 1
    if "Кот" in string or "кот" in string:
        print(counter)