# Алексей Головлев, группа БСБО-07-19
#folder_path, cell


is_allowed = True
cell_check = True
check = ""
permitted_folders = []
for _ in range(int(input())):
    folder_path_permitted = input()
    if "." not in folder_path_permitted.split("/")[-1]:
        folder_path_permitted += "/*"
    permitted_folders.append(folder_path_permitted)

read_request = [input() for _ in range(int(input()))]

print("PERMITTED FOLDERS", permitted_folders)
print("READ REQUEST", read_request)

for folder_path_read in read_request:
    check = "/"
    folder_path = folder_path_read.split("/")[1::]
    print("\n\n\n\n\n\n")
    print("FOLDER PATH", folder_path)
    for cell_read in folder_path:
        print("\n")
        print("CELL READ", cell_read)
        print("\n")
        for folder_path_permitted in permitted_folders:
            print("FOLDER PATH PERMITED", folder_path_permitted)
            for cell_permitted in folder_path_permitted.split("/")[1::]:
                print("CELL PERMITTED", cell_permitted, ",is allowed: ", is_allowed)
                if (cell_read == cell_permitted):
                    cell_check = True
                    print("== and allowed, is allowed = ", is_allowed, ",cell check = ", cell_check)
                    break

                if (cell_permitted == "*" or ("." in cell_read)) and cell_check:
                    cell_check = True
                    print("*or., is allowed = ", is_allowed, ",cell check = ", cell_check)
                else:
                    cell_check = False
                    print("else, is allowed = ", is_allowed, ",cell check = ", cell_check)
            if cell_check:
                is_allowed = True
                break
            else:
                is_allowed = False
    if is_allowed:
        print("YES___________________________________________________")
    else:
        print("NO___________________________________________________")




###ответ да нет да