# Алексей Головлев, группа БСБО-07-19

birthday_calendar = [input().split() for _ in range(int(input()))]
birthday_calendar.sort(key=lambda x: (int(x[1]), x[0]))
for i in range(int(input())):
    month = input()
    print(*[f'{i[0]} {i[1]}' for i in birthday_calendar if i[2] == month])
