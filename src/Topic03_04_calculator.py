print("MathHomework.py")
problem = input("введите задачу или 'q', чтобы выйти: ")
while (problem != "q"):
    print("ответ на ", problem, "- это", eval(problem))
    problem = input("введите задачу или 'q', чтобы выйти: ")
