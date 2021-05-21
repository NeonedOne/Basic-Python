# Алексей Головлев, группа БСБО-07-19

def bracket_check(text):
    while '()' in text:
        text = text.replace('()', '')
    if text == '':
        print('YES')
    else:
        print('NO')


bracket_check('()')
bracket_check('(()((')
