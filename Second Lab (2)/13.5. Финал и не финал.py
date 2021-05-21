# Алексей Головлев, группа БСБО-07-19

participant_list = [[input(), int(input())] for i in range(int(input()))]

for i in range(len(participant_list) - 1):
    for j in range(len(participant_list) - i - 1):
        if participant_list[j][1] > participant_list[j + 1][1]:
            participant_list[j], participant_list[j + 1] = participant_list[j + 1], participant_list[j]

finalists = participant_list[len(participant_list) // 2]
first = participant_list[: len(participant_list) // 2]

for i in range(len(finalists) - 1):
    for j in range(len(finalists) - i - 1):
        if finalists[j] > finalists[j + 1]:
            finalists[j], finalists[j + 1] = finalists[j + 1], finalists[j]

for i in finalists:
    print(i[0])

for i in range(len(first) - 1):
    for j in range(len(first) - i - 1):
        if first[j] > first[j + 1]:
            first[j], first[j + 1] = first[j + 1], first[j]

for i in first:
    print(i[0])
