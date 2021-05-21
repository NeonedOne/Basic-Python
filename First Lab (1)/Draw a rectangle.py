# Алексей Головлев, группа БСБО-07-19

length = int(input("длина:"))
width = int(input("ширина:"))
symbol = input("символ:")

for i in range(length):
    if i == 0 or i == -1:
        for j in range(width):
            if (j == 0) or (j == width-1):
                print(symbol * length)
            else:
                print(symbol + " " * (length - 2) + symbol)
