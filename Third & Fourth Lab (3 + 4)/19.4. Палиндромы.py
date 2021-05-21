# Алексей Головлев, группа БСБО-07-19

def palindrome(data):
    data = data.replace(' ', '').lower()
    return 'Палиндром' if data == data[::-1] else 'Не палиндром'


print(palindrome('12321'))
print(palindrome('Палиндром'))
