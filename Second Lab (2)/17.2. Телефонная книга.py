# Алексей Головлев, группа БСБО-07-19

phone_book = {}
for i in range(int(input())):
    data = input().split()
    if data[1] not in phone_book:
        phone_book[data[1]] = [data[0]]
    else:
        phone_book[data[1]].append(data[0])
for i in range(int(input())):
    name = input()
    print(*phone_book.get(name, ['Нет в телефонной книге']))
