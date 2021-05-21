# Алексей Головлев, группа БСБО-07-19

def fun():
    words = []
    for word in iter(input, ''):
        gem = sum(ord(w) - ord('A') + 1
                  for w in word.upper())
        words.append([gem, word])
    return sorted(words)


print(*[w[1] for w in fun()], sep='\n')




