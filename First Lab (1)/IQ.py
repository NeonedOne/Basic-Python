# Алексей Головлев, группа БСБО-07-19

num_of_people = int(input())
iq_average = 0
for i in range(1, num_of_people + 1):
    iq = int(input())
    iq_average += iq
    if iq == (iq_average / i):
        print('0')
    elif iq < (iq_average / i):
        print('<')
    elif iq > (iq_average / i):
        print('>')
