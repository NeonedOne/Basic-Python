# Алексей Головлев, группа БСБО-07-19

import math

summator = 0
num = int(input())

for i in range(1, num + 1):
    summator = i ** -2 + summator
print(math.pi ** 2 / summator)
