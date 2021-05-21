# Алексей Головлев, группа БСБО-07-19

queue = []

for i in range(int(input())):
    message = list(input().split())
    if "встал" in message or "встала" in message:
        queue.append(message[0])
    elif "Привет," in message:
        queue.insert(queue.index(message[1].replace("!", "")) + 1, message[2])
    elif "хватит" in message:
        queue.remove(message[0].replace(",", ""))

print(queue)
