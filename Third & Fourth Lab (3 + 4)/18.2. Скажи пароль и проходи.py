# Алексей Головлев, группа БСБО-07-19

def ask_password():
    for i in range(3):
        s = input()
        if s == 'password':
            print('Пароль принят')
            break
        if i == 2:
            print("В доступе отказано")


ask_password()
