# Алексей Головлев, группа БСБО-07-19

nums = list(map(int, input().split()))
graph = []
graph_length = len(nums)
graph_height = max(nums)
line = "*"

for i in range(graph_height):
    for num in nums:
        if num >= i + 1:
            line += "*"
        else:
            line += " "
    line += "*"
    graph.append(line)
    line = "*"
graph.append("*" + " " * graph_length + "*")
graph.append("*" * (graph_length + 2))

print(*(reversed(graph)), sep="\n")