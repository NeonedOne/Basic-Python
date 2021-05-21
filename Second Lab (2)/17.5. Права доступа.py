# Алексей Головлев, группа БСБО-07-19
#folder_path, cell


data = {}
for i in range(int(input())):
    path_permitted = input()
    data[path_permitted] = data.get(path_permitted)
for i in range(int(input())):
    path_to_read = ''
    user_is_permitted = False
    for i in input().split('/'):
        if i:
            path_to_read = path_to_read + '/' + i
        if path_to_read in data:
            user_is_permitted = True
    if user_is_permitted:
        print('YES')
    else:
        print('NO')
