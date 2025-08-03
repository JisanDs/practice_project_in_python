import random

numVlue = {
    1: "Snake",
    2: "Water",
    3: "Gun"
}

print("Welcome to Snake_Water_Gun game")

while True:
    try:
        user = input("Choose a number between: 1, 2, 3 or (Quit/Q): ")

        if user.lower() in ('q', 'quit'):
            print("Thanks for playing game🙂!")
            break

        user = int(user)
        if user not in numVlue:
            print("Invalid choice! Please enter 1, 2, or 3🥲")
            continue

        game_guess = random.randint(1, 3)
        
        print("Game choose:", numVlue[game_guess])
        print("You choose:", numVlue[user])
        
        if user == game_guess:
            print("Game is draw😄!")
        elif (user == 1 and game_guess == 2) or \
             (user == 3 and game_guess == 1) or \
             (user == 2 and game_guess == 3):
            print("You win😊!")
        else:
            print("Computer win😁!")

    except ValueError:
        print("Please enter a valid number (1, 2, 3) or Q to quit🥲")