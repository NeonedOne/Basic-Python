# Алексей Головлев, группа БСБО-07-19

num_of_mistakes = int(input("запас терпения учителя: "))
right_result = ["раз", "два", "три", "четыре"]
counter = 0
iterator = 0

while num_of_mistakes !=0:
    input_result = input("")
    if input_result == right_result[iterator]:
        counter += 1
        if iterator == 3:
            iterator = 0
        else:
            iterator += 1
    else:
        print("Правильных отсчётов было " + str(counter) + ", но теперь вы ошиблись")
        num_of_mistakes -= 1
        counter = 0
        iterator = 0
if num_of_mistakes == 0:
    print("На сегодня хватит.")