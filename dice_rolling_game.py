import random

print("Welcome to Dice Rolling Game!")
while True:
    choise = input("Roll the dice(y/n): ").lower()
    if choise == "y":
        dice1 = random.randint(1, 6)
        dict2 = random.randint(1, 6)
        print(f"({dice1}, {dict2})")
    elif choise == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choise!")