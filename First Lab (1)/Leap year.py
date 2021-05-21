# Алексей Головлев, группа БСБО-07-19

year = int(input())

if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    print("LEAP")
else:
    print("NO")
