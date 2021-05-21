# Алексей Головлев, группа БСБО-07-19

data = [list(map(int,input().split())) for i in range(int(input()))]
chars = {}
median_list = []
mod_list = []
ultra_data = []

for sets in data:
    median_list.append(sets[len(sets)//2])
    for i in sets:
        ultra_data.append(i)
        chars.update({sets.count(i): i})
    mod_list.append((max(chars.items())[1]))
print(*median_list)
print(*mod_list)
chars.clear()

print(median_list[len(median_list)//2])
for mod in mod_list:
    chars.update({mod_list.count(mod): mod})
print((max(chars.items())[1]))
chars.clear()

print(ultra_data[len(ultra_data)//2])
for mod in ultra_data:
    chars.update({ultra_data.count(mod): mod})
print((max(chars.items())[1]))