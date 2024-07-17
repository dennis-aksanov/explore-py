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
fruit = input('choose fruit: \n  ')
print("you choose {}".format(fruit))
if None != fruits.get(fruit):
    print("i have {} {}".format(fruits[fruit], fruit))
else:
    print("i don't have {} fruit".format(fruit))

fet = input('how many fruits do you want?\n  ')
fet = int(fet)
if fruits.get(fruit) >= fet:
    print('yes i can give you {} fruits'.format(fet))
else:
    print("sorry i don't have enough fruits")

