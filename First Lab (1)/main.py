# Алексей Головлев, группа БСБО-07-19


print('Добро пожаловать в Квест.')
print('Вы очнулись в незнакомом помещение')
print('Перед вами 3 двери с номерами: 1, 2 или 3.')
print('Дверь из которой можно выбраться - не крайняя, в какую пройдете?')
otv1 = input()
if otv1 == '3':
    print('Пройдя в эту дверь, она захлопнулась. Выхода нет. Game over.')
elif otv1 == '1':
    print('Вы прошли в пропасть')
if otv1 == '2':
    print('Вы в следующей комнате')
    print('Выход отсюда возможен через 2 двери.')
    print('Дверь справа под номером 1, дверь слева под номером 2,')
    print('над дверью слева написано: выход в двери под номером 2.')
    print('Выход справа или слева?')
    otv2 = input()
    if otv2 == 'справа':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегала ')
        print('гигантская подземная жаба, которая проглотила вас целиком!')
    elif otv2 == 'слева':
        print('Вы на улице!')