# Алексей Головлев, группа БСБО-07-19

step = int(input())
text = input()
result = ''

alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдежзийклмнопрстуфхцчшщъыьэюя"

for i in text:
    if i in alphabet:
        char_position = alphabet.find(i)
        key = char_position + step
        if key > len(alphabet):
            key = key % 64
        elif key < 0:
            key = key % 64
        result += alphabet[key]
    else:
        result += i
print(result)