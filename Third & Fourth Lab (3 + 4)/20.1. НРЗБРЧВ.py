# Алексей Головлев, группа БСБО-07-19

translatedText = ''


def translate(text):
    global translatedText
    redLetter = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е',
                 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е',
                 '.', ',', '-']
    for i in range(len(text) - 1):
        if redLetter.count(text[i]) == 0:
            translatedText = translatedText + text[i]
    translatedText = ' '.join(translatedText.split())
    print(translatedText)


translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно' +
          'просто читать. Достаточно небольшой тренировки - и вы сможете это делать.')
