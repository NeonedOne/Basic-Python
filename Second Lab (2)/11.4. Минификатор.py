# Алексей Головлев, группа БСБО-07-19

for i in range(int(input())):
    text, result_text, wrong_spaces = input(), "", ""
    open_quotes_checker, space_checker, slash_checker, tabulation_checker,breaked_space = False, False, False, False, False

    if text.count("\'") == 0 and text.count("\"") == 0 and text.count("#") == 0:
        text = ' '.join(text.split())
        print(text, end="")

    else:
        for char in text:
            if char != " ":
                if space_checker:
                    space_checker = False
                    tabulation_checker = False
                    breaked_space = False
            if char == "\"" or char == "\'":
                open_quotes_checker = not open_quotes_checker
            if char == " ":
                if space_checker and not open_quotes_checker:
                    breaked_space = True
                space_checker = True
                if char == text[0]:
                    tabulation_checker = True
            if not open_quotes_checker:
                if char == "#":
                    break
                if space_checker:
                    if tabulation_checker:
                        pass


            if not breaked_space: result_text += char
    print(result_text)
