# Алексей Головлев, группа БСБО-07-19

def defractalize(fractal):
    while fractal in fractal:
        fractal.remove(fractal)


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
defractalize(fractal)
print(fractal)
print()


fractal = [2, 5]
fractal.append(fractal)
fractal.append(3)
fractal.append(fractal)
fractal.append(9)
defractalize(fractal)
print(fractal)
