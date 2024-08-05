import sys
from array import array

dishes = {
          1: "Кукурузная каша",
          2: "Гречневая каша",
          3: "Геркулесовая каша",
          4: "Пшёная каша",
          5: "Пшеничная каша",
          6: "Блины",
          7: "Омлет",
          8: "Манная каша",
          9: "Кофе"}

CountPeople = 5
choisesCount = 3
dishesCount = len(dishes)

choises = {}


def ShowMenu(dishes):
    print("0 - выход")
    for key, val in dishes.items():
        print("{} - {}".format(key, val))


def AskChoise(prompt, minKey, maxKey):
    key = -1
    while key < minKey or key > maxKey:
        raw = input("{} [{} - 9]: ".format(prompt, minKey))
        try:
            key = int(raw)
        except ValueError:
            print("{} - не коректно.".format(raw))
    return key


def Calculate(choises):
    result = dict({})
    for person, personChoises in choises.items():
        for rec in personChoises:
            key = list(rec.keys())[0]
            result[key] = result.setdefault(key, 0) + rec[key]
    return result


def ShowResult(calculated, dishes):
    print("\n Результат голосования:")
    for dish, count in calculated.items():
        print("    {} - {}".format(dishes[dish], count/(100/choisesCount)))


def main():
    for person in range(CountPeople):
        ShowMenu(dishes)
        choises[person] = []
        chosenDishes = [-1] * choisesCount

        print("Участник голосования номер {}".format(person + 1))

        for dishNumber in range(choisesCount):
            askAgain = True
            while askAgain:
                chosenDish = AskChoise("Выберите {} блюдо".format(dishNumber + 1), 0, len(dishes))
                # if chosenDish > 9:
                #     print("{} - не коректно.".format(chosenDish))
                if chosenDish == 0:
                    answer = input("Точно вы хотите выйти (Yes / No)? ")
                    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
                        exit(0)

                chosenDishes[dishNumber] = chosenDish
                askAgain = False
                for d in range(dishNumber):
                    if chosenDishes[d] == chosenDish:
                        askAgain = True
                        break
                if not askAgain:
                    choises[person].append({chosenDish: 100/choisesCount})
    calculated = Calculate(choises)
    ShowResult(calculated, dishes)


if __name__ == "__main__":
    main()
    sys.exit()
