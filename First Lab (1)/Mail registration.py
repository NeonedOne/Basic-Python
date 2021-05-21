#Алексей Головлев, группа БСБО-07-19

print('Enter your name: ')
name = input()
print('Enter your email: ')
email = input()
if ('@' in name):
    print('Некорректный логин')
if ('@' not in email):
    print('Некорректный адрес')
else:
    print('OK')