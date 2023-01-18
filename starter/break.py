for letter in "supercalifragilisticexpialidocious":
    if letter == 'c':
        break
    print(letter)

message = input("say hi: ")
while True:
    if message == "hi":
        break
    message = input("say hi: ")


for letter in "supercalifragilisticexpialidocious":
    if letter in 'aeiou':
        continue
    print(letter)
