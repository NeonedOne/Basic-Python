# Алексей Головлев, группа БСБО-07-19

for i in range(int(input())):
    text = input()
    if text[0] and text[1] == "%":
        print(text[2:])
    elif (text[0] and text[1] and text[2] and text[3]) == "#":
        pass
    else:
        print(text)
