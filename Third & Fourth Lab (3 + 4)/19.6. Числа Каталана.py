# Алексей Головлев, группа БСБО-07-19

import math


def catalan(n):
    return int((math.factorial(2 * n)) // (math.factorial(n) * math.factorial(n + 1)))


print(catalan(0))
print(catalan(1))
