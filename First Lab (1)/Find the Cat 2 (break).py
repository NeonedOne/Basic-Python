# Алексей Головлев, группа БСБО-07-19

counter = 0
checker = True
string = "nothing"

while string != "СТОП":
    string = input()
    counter += 1
    if "Кот" in string or "кот" in string:
        print(counter)
        checker = False
        break
if checker:
    print(-1)
