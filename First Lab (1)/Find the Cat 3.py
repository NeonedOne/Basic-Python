# Алексей Головлев, группа БСБО-07-19

counter_of_strings = 0
num_of_1st_string = 0
counter = 0
checker = True
string = "nothing"

while string != "СТОП":
    string = input()
    counter_of_strings += 1
    if "Кот" in string or "кот" in string:
        if checker:
            num_of_1st_string = counter_of_strings
            checker = False
        counter += 1
if checker:
    print(0, -1)
else:
    print(counter, num_of_1st_string)