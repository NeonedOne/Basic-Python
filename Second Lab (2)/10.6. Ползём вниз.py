# Алексей Головлев, группа БСБО-07-19

instruction = input()
char = instruction[0]
sym = '>'
count, max_l = 1, 0
for i in range(len(instruction)):
    if instruction[i] == '>':
        count += 1
        max_l = count
    if instruction[i - 1] == '>' and instruction[i] != '>':
        for j in range(max_l):
            print(end=char)
        print()
    if instruction[i - 1] == 'V' and (instruction[i] == 'V' or instruction[i] == '>'):
        for j in range(max_l - 1):
            print(end=' ')
        print(char)
    if instruction[i] == '<':
        count -= 1
    if instruction[i - 1] == '<' and (instruction[i] != '<' or i == len(instruction) - 1):
        for j in range(max_l - count):
            print(end=' ')
        for j in range(max_l):
            print(end=char)
        print()