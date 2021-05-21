pool1 = int(input("Сколько камней в 1 куче? "))
pool2 = int(input("Сколько камней во 2 куче? "))
pool3 = int(input("Сколько камней в 3 куче? "))
nim = pool1 ^ pool2 ^ pool3
step = 0
if nim > 0:
    if pool1 ^ nim < pool1:
        dif = pool1 - (pool1 ^ nim)
        pool1 -= dif
        get = pool1
        num = 1
    elif pool2 ^ nim < pool2:
        dif = pool2 - (pool2 ^ nim)
        pool2 -= dif
        get = pool2
        num = 2
    else:
        dif = pool3 - (pool3 ^ nim)
        pool3 -= dif
        get = pool3
        num = 3
else:
    pool1 -= 1
    dif = 1
    num = 1
    get = pool1
print("Я забрал " + str(dif) + " камней из " + str(num) + " кучи, теперь там " + str(get) + " камней. Твой ход")
while pool1 + pool2 + pool3 > 0:
    step = 2
    num = 0
    while num < 1 or num > 3:
        num = int(input("Из какой кучи? "))
        if num == 1 and pool1 == 0 or num == 2 and pool2 == 0 or num == 3 and pool3 == 0:
            print("Здесь уже нет камней!")
            num = 0
    con = True
    while con:
        if num == 1:
            get = pool1
        elif num == 2:
            get = pool2
        else:
            get = pool3
        dif = int(input("Сколько (но не больше " + str(get) + ")?"))
        if dif > 0 and dif <= get:
            if num == 1:
                pool1 -= dif
                get = pool1
            elif num == 2:
                pool2 -= dif
                get = pool2
            else:
                pool3 -= dif
                get = pool3
            print("ВЫ взяли " + str(dif) + " камней из " + str(num) + " кучи, теперь там " + str(
                get) + " камней. Не твой ход")
            con = False
    if pool1 + pool2 + pool3 > 0:
        step = 1
        nim = pool1 ^ pool2 ^ pool3
        if nim > 0:
            if pool1 ^ nim < pool1:
                dif = pool1 - (pool1 ^ nim)
                pool1 -= dif
                get = pool1
                num = 1
            elif pool2 ^ nim < pool2:
                dif = pool2 - (pool2 ^ nim)
                pool2 -= dif
                get = pool2
                num = 2
            else:
                dif = pool3 - (pool3 ^ nim)
                pool3 -= dif
                get = pool3
                num = 3
        else:
            if pool1 > 0:
                pool1 -= 1
                num = 1
                get = pool1
            elif pool2 > 0:
                pool2 -= 1
                num = 2
                get = pool2
            else:
                pool3 -= 1
                num = 3
                get = pool3
            dif = 1
        print("Я взял " + str(dif) + " камней из " + str(num) + " кучи, теперь там " + str(get) + " камней. Ваш ход")
if step == 1:
    print("Не победа")
else:
    print("Победа")
