import random

number = random.randint(1,101)

def easy_guess():
    for _ in range(10):
        user_guess = int(input("Guess a number between 1 to 100 : "))
        if user_guess == number:
            print(f"You got it! 🎉 The number is {number}")
            break
        elif user_guess > number:
            if _ == 9:
                print(f"Too high. 🔼 You have {9-_} attempts remaining to guess the number. ")
            else:
                print(f"Too high. 🔼 Guess again. \nYou have {9-_} attempts remaining to guess the number. ")
        elif user_guess < number:
            if _ == 9:
                print(f"Too low. 🔽 You have {9-_} attempts remaining to guess the number. ")
            else:
                print(f"Too low. 🔽 Guess again. \nYou have {9-_} attempts remaining to guess the number. ")
    else:
        print(f"You have run out of guesses, you lose. 😔\nThe number is {number}")
    

def hard_guess():
    for _ in range(5):
        user_guess = int(input("Guess a number between 1 to 100 : "))
        if user_guess == number:
            print(f"You got it! 🎉 The number is {number}")
            break
        elif user_guess > number:
            if _ == 4:
                print(f"Too high. 🔼 You have {4-_} attempts remaining to guess the number. ")
            else:
                print(f"Too high. 🔼 Guess again. \nYou have {4-_} attempts remaining to guess the number. ")
        elif user_guess < number:
            if _ == 4:
                print(f"Too low. 🔽 You have {4-_} attempts remaining to guess the number. ")
            else:
                print(f"Too low. 🔽 Guess again. \nYou have {4-_} attempts remaining to guess the number. ")
    else:
        print(f"You have run out of guesses, you lose. 😔\nThe number is {number}")

print("\n  ==================== WELCOME TO NUMBER GUESSING GAME ====================\n")

ask = input("Do you want to choose the game easy or hard? ").lower()

if ask == "easy":
    easy_guess()
elif ask == "hard":
    hard_guess()
else:
    print("Sorry, Your choice is not valid ")
