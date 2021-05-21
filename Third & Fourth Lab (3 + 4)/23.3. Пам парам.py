# Алексей Головлев, группа БСБО-07-19

line = input()
lines = line.split()


def rhythm(lines):
    lst = [sum(x in 'уеыаоэяию' for x in lin)
           for lin in lines]
    if len(set(lst)) == 1:
        res = "Парам пам-пам"
    else:
        res = "Пам парам"
    print(res)


rhythm(lines)
