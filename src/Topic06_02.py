import random
choices = {1: "камень",
           2: "ножницы",
           3: "бумага"}

print("к>н,н>б,б>к")
player = 4
while player != 0:
    raw = input("выбирите: 1-камень, 2-ножницы, 3-бумага или 0-(выйти)? ")
    try:
        player = int(raw)
    except ValueError:
        print("{} -- не число.".format(raw))
        continue

    if player == 0:
        break

    if player > 3 or player < 0:
        print("в списке нет такого выбора")
        continue

    computer = random.randrange(1, 4)
    print("Твой выбор {}, компьютер выбрал {}.".format(choices[player], choices[computer]))


    if player == computer:
        print("ничья")
    elif player == 1 and computer == 2 \
            or player == 2 and computer == 3 \
            or player == 3 and computer == 1:
        print("вы победили")
    else:
        print("компьютер победил")

    # elif player == "ножницы":
    #     if computer == "бумага":
    #         print("вы победили")
    #     else:
    #         print("компьютер победил")
    # elif player == "бумага":
    #     if computer == "камень":
    #         print("вы победили")
    #     else:
    #         print("компьютер победил")
    # else:
    # print("в списке нет такого выбора")
    # print()
    # player = input("выбирите: 1-камень, 2-ножницы, 3-бумага или "
    #                "0-2(выйти)? ")