# Алексей Головлев, группа БСБО-07-19

message = input()
cost = (len(message) * 0.4)
print(int(cost // 1), 'р.', int((cost - int(cost // 1)) * 100), 'коп.')
