# Алексей Головлев, группа БСБО-07-19

import math


def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return ['all']
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        return [(c * (-1)) / b]
    elif b == 0:
        return [math.sqrt((-1 * b) / a)]
    elif c == 0:
        return [0, (-1 * b) / a]
    else:
        q = b ** 2
        w = -4 * a * c
        D = q + w
        if D < 0:
            return []
        elif D == 0:
            return [(-1 * b) / (2 * a)]
        else:
            D = math.sqrt(D)
            return [int(((-1 * b) - D) / (2 * a)), ((-1 * b) + D) / (2 * a)]


def solve(*coefficients):
    if len(coefficients) == 3:
        return roots_of_quadratic_equation(coefficients[0], coefficients[1], coefficients[2])
    elif len(coefficients) == 2:
        return roots_of_quadratic_equation(0, coefficients[0], coefficients[1])
    elif len(coefficients) == 1:
        return roots_of_quadratic_equation(0, 0, coefficients[0])
    else:
        return None


nums = input().split()
nums = [int(x) for x in nums]
print(*sorted(solve(*nums)), sep=" ")
