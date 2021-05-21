# Алексей Головлев, группа БСБО-07-19

tape = [0 for _ in range(30001)]
position = 0
f = False
s = False
for cmd in input():
    test = tape[position]
    if cmd == '[':
        f = True
    elif cmd == ']':
        s = True
    elif f and not s and cmd == '-':
        tape[position] = 1
    if f and s:
        f = False
        s = False
    elif cmd == '>':
        position += 1
    elif cmd == '<':
        position -= 1
    elif cmd == '+':
        tape[position] += 1
    elif cmd == '-':
        tape[position] -= 1
    elif cmd == '.':
        print(tape[position])
    if tape[position] > 255:
        tape[position] = 0
    elif tape[position] < 0:
        tape[position] = 255
