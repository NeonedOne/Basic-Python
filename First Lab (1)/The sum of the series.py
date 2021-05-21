# Алексей Головлев, группа БСБО-07-19

num_of_itearions = int(input())
summator = 0
i = 1
for i in range(num_of_itearions):
    num = int(input())
    if i % 2 == 0:
        summator += num
    else:
        summator -= num
print(summator)