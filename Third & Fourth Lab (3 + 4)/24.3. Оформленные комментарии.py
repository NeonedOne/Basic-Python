# Алексей Головлев, группа БСБО-07-19

import re


def get_code():
    code = ''
    line = ''
    while line != '\n':
        code += line
        line = input() + '\n'
    return code;


def format_comments(code):
    for lineno, line in enumerate(code.splitlines(), 1):
        yield f'Line {lineno}:{re.search(r"#(.+)", line)[1]}';


def print_comments(code):
    print(*format_comments(code), sep='\n')


def print_code_comments():
    code = get_code()
    print_comments(code)


print_code_comments()
