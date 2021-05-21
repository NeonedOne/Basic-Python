# Алексей Головлев, группа БСБО-07-19

recipe = [input() for i in range(int(input()))]
for instruction in recipe:
    if "лук" in instruction:
        recipe.remove(instruction)
print(*recipe, sep=", ")