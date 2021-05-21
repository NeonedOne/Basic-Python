# Алексей Головлев, группа БСБО-07-19

def prime(number):
    n = number
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    return 'Простое число' if counter == 2 else 'Составное число'


print(prime(4))
print(prime(3))
