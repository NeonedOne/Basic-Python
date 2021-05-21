# Алексей Головлев, группа БСБО-07-19

list_products_we_have = []
list_of_recipe_temp = []
summator = 0

m = int(input())
for i in range(m):
    list_products_we_have.append(input())
list_products_we_have.sort()

n = int(input())
for i in range(n):
    name_of_recipe = (input())
    amount_of_products = int(input())
    for j in range(amount_of_products):
        list_of_recipe_temp.append(input())
    if set(sorted(list_products_we_have)) & set(sorted(list_of_recipe_temp)) == set(sorted(list_of_recipe_temp)):
        print(name_of_recipe)
    list_of_recipe_temp.clear()
