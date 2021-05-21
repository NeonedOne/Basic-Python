# Алексей Головлев, группа БСБО-07-19

letter = input()
text = list(input().split())
for words in text:
    if letter in words.lower():
        print(words)