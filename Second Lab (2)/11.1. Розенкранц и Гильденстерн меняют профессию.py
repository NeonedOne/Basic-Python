# Алексей Головлев, группа БСБО-07-19

result = input()
count = 0
max_count = 0
for i in result:
    if i == "о":
        count += 1
        if count > max_count:
            max_count = count
    else:
        count = 0
print(max_count)