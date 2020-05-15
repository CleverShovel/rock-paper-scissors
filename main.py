from random import randint


name = input("Enter your name: ")
print(f"Hello, {name}")

options = input()
options = options.split(',') if options else ['rock', 'paper', 'scissors']

rating = 0
rating_file = open('rating.txt', 'r', encoding='utf-8')
for line in rating_file:
    splits = line.split()
    if splits[0] == name:
        rating = int(splits[1])
        break;

print("Okay, let's start")

while True:
    command = input()
    
    if command == "!exit":
        print("Bye!")
        break
    elif command == "!rating":
        print(f"Your rating: {rating}")
        continue
    elif command not in options:
        print("Invalid input")
        continue

    player = options.index(command)

    computer = randint(1, len(options)) - 1

    result = ""
    if player == computer:
        rating += 50
        result = "There is a draw ({})"
    elif player + (len(options) if player < computer else 0) <= (computer + len(options) / 2):
        rating += 100
        result = "Well done. Computer chose {} and failed"
    else:
        result = "Sorry, but computer chose {}"

    print(result.format(options[computer]))