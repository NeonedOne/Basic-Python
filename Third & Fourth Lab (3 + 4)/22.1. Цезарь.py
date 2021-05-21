# Алексей Головлев, группа БСБО-07-19

def encrypt_caesar(msg, shift):
    small_symbols1 = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
    big_symbols1 = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    shift = shift % len(small_symbols1)
    small_symbols2 = small_symbols1[shift:] + small_symbols1[:shift]
    big_symbols2 = big_symbols1[shift:] + big_symbols1[:shift]
    translation = msg.maketrans(small_symbols1 + big_symbols1, small_symbols2 + big_symbols2)
    return msg.translate(translation)


def decrypt_caesar(msg, shift):
    return encrypt_caesar(msg, -1 * shift)


msg = 'Да здравствует салат Цезарь!'
shift = 3
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
print()

msg = 'Да здравствует салат Цезарь!'
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)
