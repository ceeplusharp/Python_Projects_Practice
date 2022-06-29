# A simple take on the number guessing game.
# Guess from positive integers with hints of higher or lower.

from random import randint

# Initialize variables for game tracking
guess_count = 0
game_guess = []

# While loop to prompt the user for the maximum number for the range of the choices.
while True:
    # Incorporated try-except block to display error message for when the user
    # enters invalid input for maximum range.
    try:
        max_number = input("\nPlease enter the maximum number for the range of the choices (1, maximum): ")
        if int(max_number) > 1:
            random_number = randint(1, int(max_number)+1)  # Random number generator.
            break
        else:
            print("Please choose a number higher than 1.")
            continue
    except ValueError:
        print("Invalid input. Please enter positive integers only.")

# While loop for the user to keep guessing until deciding to quit.
while True:
    
    # Prompts the guess number of the user.
    number_guess = input(f"\nWhat is the random number from 1 to {max_number}?"
                     "\n(Enter 'q' anytime to quit.)"
                     "\nPlease enter your guess: ")
    
    # Prompt for the program to quit when the user decides to.
    if number_guess == 'q':
        print("\n***Player has quit.***\n"
              "\nThank you for playing!\n")
        break
    elif number_guess != None:
        # Incorporated try-except block to display error message for when the user
        # enters non-numerical value other than 'q' for quitting the program.
        try:
            # Convert the input into an integer so it can be use for hint calculations.
            number_guess = int(number_guess)
            game_guess.append(number_guess)
            guess_count += 1
            
            # Simple if-elif statements for hints and winning messages.
            if number_guess > int(max_number):
                print("Oops. Your chosen number is already higher than the maximum range.")
                continue
            elif number_guess < 0:
                print("Invalid input. Please enter positive integers only.")
                game_guess.remove(number_guess)
                guess_count -= 1
                continue
            elif number_guess < random_number:
                print("Try a higher number.")
                continue
            elif number_guess > random_number:
                print("Try a lower number.")
                continue
            elif random_number == number_guess:
                print(f"The random number: {random_number}"
                    "\nYou hit the jackpot!!!\n")
                break
        except ValueError:
            print("Invalid input. Please enter positive integers only.")

print(f"Guess history: {game_guess}")
print(f"Total count of guess: {guess_count}\n")
