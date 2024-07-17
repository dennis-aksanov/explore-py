# name = ''
# while name != 'exit':

fruits = {
    "banana":     10,
    "apple":      3,
    "watermelon": 1,
    "pear":       7}


name = input('Type your name: \n  ')
print("Hello, {}".format(name))
print("how are you {}".format(name))
det = input(' ')

isFruitChoosen = False
while isFruitChoosen == False:
    fruit = input('choose fruit: \n  ')
    print("you choose {}".format(fruit))
    if None != fruits.get(fruit):
        print("i have {} {}".format(fruits[fruit], fruit))
        isFruitChoosen = True
    else:
        print("i don't have {} ".format(fruit))
        fer = input("do you want choose another one? (yes/no)\n  ")
        if fer == "yes":
           isFruitChoosen = False
        else:
            exit()
fet = input('how many {} do you want?\n  '.format(fruit))
fet = int(fet)
if fruits.get(fruit) >= fet and 0 <= fet:
    print('yes i can give you {} {}'.format(fet, fruit))
    fruits[fruit] = fruits[fruit] - fet
    print("now i have {}".format(fruits[fruit]))
else:
    print("sorry i don't have enough {}".format(fruit))

