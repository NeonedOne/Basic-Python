# Алексей Головлев, группа БСБО-07-19

def line(s, t):
    if '+' in s:
        equation = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(s[s.find('+'):])
    else:
        aaa = s[s.find('x'):]
        equation = float(s[:s.find('x')]) * float(t[:t.find(';')]) + float(aaa[aaa.find('-'):])
    if float(t[t.find(';') + 1:]) == equation:
        print(True)
    else:
        print(False)


line('1x+6', '1;7')
line('5x-10', '5;-9')
line('0x+7', '3;7')
line('3.5x+0', '2;7')
