# Алексей Головлев, группа БСБО-07-19

data = []
information = list(input().split(":"))
while information != [""]:
    data.append(information)
    information = list(input().split(":"))
exception = list(input().split(";"))
for i in range(len(data)):
    if exception.count(data[i][1]) != 0:
        print("To:", data[i][0])
        worker_name = data[i][4].split(",")
        print(worker_name[0] + "," + " ваш пароль слишком простой, смените его.")
