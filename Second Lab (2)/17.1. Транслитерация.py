# Алексей Головлев, группа БСБО-07-19

transliteration = {'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh',
                   'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O',
                   'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc',
                   'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia', 'а': 'a',
                   'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z',
                   'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
                   'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'tc', 'ч': 'ch', 'ш': 'sh',
                   'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'iu', 'я': 'ia'}
result = []
changed_letter = ''
text = input()
text = text.split()
for i in range(len(text)):
    word = text[i]
    for letter_index in range(len(word)):
        if word[letter_index] in transliteration:
            changed_letter += transliteration[word[letter_index]]
        else:
            if word[letter_index] == 'ъ' or word[letter_index] == 'ь' or word[letter_index] == 'Ъ' or word[letter_index] == 'Ь':
                continue
            else:
                changed_letter += word[letter_index]
    if len(changed_letter) != 0:
        result.append(changed_letter)
        changed_letter = ''
print(*result)
