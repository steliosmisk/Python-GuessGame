import random

print("--WELCOME TO GUESSING GAME--")
print("[1] Start The Game")
print("[2] Exit")

# AI Choose a number
ai = random.randrange(0, 100)

win = 0
attempts = 0

user_choice = input("Enter (1/2): ")
while user_choice == '1' and user_choice != '2':
    try:
        # User Choose a number
        user_number = int(input("Guess the number: "))
        print(f"Wins: {win} | Attempts: {attempts}")
        if user_number >= 101 or user_number <= -1:
            print("Enter a valid guess! from 0 to 100!")
        elif user_number == ai:
            win += 1
            print(f"Crap, You found my number. You: {user_number} | AI: {ai}")
            break
        elif user_number > ai:
            attempts += 1
            print("Lower :)")
        elif user_number < ai:
            attempts += 1
            print("Higher :)")
    except ValueError:
        print("Enter a number not a string!")
