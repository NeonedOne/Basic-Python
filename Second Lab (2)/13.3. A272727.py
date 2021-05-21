sequence = [0]
for i in range(int(input())):
    count = 0
    for j in range(len(sequence)):
        if sequence[j] == sequence[-j - 1]:
            count += 1
    sequence.append(count)
print(*sequence[:-1], sep= "\n")