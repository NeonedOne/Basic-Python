# Алексей Головлев, группа БСБО-07-19

whitelist = []
for i in range(int(input())):
    whitelist.append(input())
for i in range(int(input())):
    search = input()
    if search in whitelist:
        print(search)