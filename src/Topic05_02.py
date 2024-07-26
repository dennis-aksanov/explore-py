key = 0
while key < 1 or key > 25:
    keyStr = input("введитте кключ длля коодированния?")
    try:
        key = int(keyStr)
    except ValueError:
        print("{} -- не число.".format(keyStr))
        key = 0
print("{}".format(key))
message = input("введите сообщение для кодировки или раскодировки:")
message = message.upper()
print("{}".format(message))
output = ""
for letter in message:
    if letter.isupper():
        value = ord(letter) + key
        letter = chr(value)
    if not letter.isupper():
        value -= 26
        letter = chr(value)
    output += letter
print("выходное сообщение: ", output)
message = ""

for letter in output:
    if letter.isupper():
        value = ord(letter) - key
        letter = chr(value)
    if not letter.isupper():
        value += 26
        letter = chr(value)
    message += letter
print("входное сообщение: ", message)
