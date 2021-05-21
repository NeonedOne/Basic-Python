# Алексей Головлев, группа БСБО-07-19

lst = [int(input()) for i in range(int(input()))]
print(*sorted(lst)[::-1], sep="\n")