# Алексей Головлев, группа БСБО-07-19

num = int(input())
counter = 0

while num != 1:
    num = 3 * num + 1 if num % 2 else num // 2
    counter += 1
print(counter)