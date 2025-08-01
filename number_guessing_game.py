import random

# Welcome message
print("Welcome to the Number Guessing Game!")
# Short intro message
print("I'm thinking of a number between 1 and 100... Can you guess it?")

#genrat random number
game_guess = random.randint(1, 100)

while True:
    user_guess = input("Guess the number or Quite(Q): ")
    if user_guess.lower() == "q":
        print("Thanks for playing!")
        break
#user guessing checking whit error handiling
    try:
        user = int(user_guess)
        if user > game_guess:
            print("Your guess is biger guess samll number: ")
        elif user < game_guess:
            print("Your guess is smaller guess big number: ")
        else:
            print(f"Congratulations! You guessed the correct number: {game_guess}")
            break
    except ValueError:
        print("Invalid choise!")

print("_________Game Over_________")