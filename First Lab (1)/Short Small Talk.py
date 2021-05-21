# Алексей Головлев, группа БСБО-07-19

answer = input("Ну что, как настроение?\n")
if "хорошее" in answer or "прекрасно" in answer:
    print("Отлично, у меня тоже всё хорошо ))")
elif "плохо" in answer or "ужасно" in answer:
    print("Ничего, скоро всё наладится")
elif "!" in answer or "?" in answer:
    print("эмоциональненько, но я не понимать")
else:
    print("ответь лаконичнее, я не понимать")