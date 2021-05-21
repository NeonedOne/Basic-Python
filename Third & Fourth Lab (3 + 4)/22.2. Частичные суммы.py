# Алексей Головлев, группа БСБО-07-19

def partial_sums(*args):
    sums = [0]
    for i, x in enumerate(args):
        sums.append(x + sums[i])
    return sums


print(partial_sums(13))
print(partial_sums(1, 0.5, 0.25, 0.125))
