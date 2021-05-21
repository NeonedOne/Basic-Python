# Алексей Головлев, группа БСБО-07-19

string = input()
chars = {}
for i in string:
    chars.update({string.count(i): i})
print((max(chars.items())[0]))