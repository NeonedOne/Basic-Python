# Алексей Головлев, группа БСБО-07-19

URL = list((input().replace("&", "?")).split("?"))
key = input()
for elements in URL:
    if key in elements:
        print(*list(elements.split("=")[1]), sep="")