# Алексей Головлев, группа БСБО-07-19

string = input()
counter = 1
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            counter += 1
        else:
            a = string[i]
            print(counter, string[i])
            counter = 1
print(counter, string[i])