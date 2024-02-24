from random import randint
from sys import exit

username = input("Your username: ")
print("Type start to play. Type quit to leave.")

def random_quiz():
    symbols = ["+", "-", "×", "÷"]
    symbol = symbols[randint(0,3)]
    numbers = [randint(0, 15), randint(0, 15)]
    if symbol == symbols[0]:
        answer = numbers[0] + numbers[1]
    elif symbol == symbols[1]:
        answer = numbers[0] - numbers[1]
    elif symbol == symbols[2]:
        answer = numbers[0] * numbers[1]
    elif symbol == symbols[3]:
        answer = numbers[0] / numbers[1]

    answer = round(answer)

    while True:
        print(f"\n  {numbers[0]}\n{symbol} {numbers[1]}\n----------------")
        uanswer = input("  ")
        try:
            if int(uanswer) == answer:
                print("\nCorrect!\n\n")
                break
            else:
                print("\n\nIncorrect, please try again.\n\n")
        except:
            if uanswer == "quit":
                exit()
            elif uanswer == "giveup":
                print(answer)
            else:
                print("\nPlease use Base 10n\n\n")

while True:
    command = input("> ").lower()
    if command == "start":
        for i in range(10):
            print(f"question {i}/10\n")
            random_quiz()
    elif command == "quit":
        exit()