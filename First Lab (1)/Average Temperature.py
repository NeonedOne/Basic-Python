# Алексей Головлев, группа БСБО-07-19

summator = 0.0
counter = -1
temp = 0
while -300.0 < temp:
    temp = float(input())
    summator += temp
    counter += 1
print("%.3f" % ((summator-temp)/counter))
