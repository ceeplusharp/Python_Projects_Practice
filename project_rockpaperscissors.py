# A simple take on the Rock, Paper, Scissors game.
# Just using if-elif-else statements and while loop.

from random import choice

# While loop for the program to keep running until the user quits.
while True:
    # Prompt for the user choice of hand.
    player_choice = input("\nChoose between rock 'R', paper 'P' or scissors 'S'."
                          "\n(Note: Please enter 'q' anytime to quit.)"
                          "\nPick your winning hand: ")
    
    # A list for variable assignments.
    choices = ['R', 'P', 'S']
    R = 'rock'
    P = 'paper'
    S = 'scissors'
    
    # Prompt for the program to quit when the user decides to.
    if player_choice == 'q':
        break
    
    # Deciding factors for the win, lose or tie.
    # Simple print functions to display the choice of the user.
    elif player_choice in choices:
        if player_choice == 'R':
            print(f"Your pick: {R}")
        elif player_choice == 'P':
            print(f"Your pick: {P}")
        elif player_choice == 'S':
            print(f"Your pick: {S}")
        
        # Simple print functions to display the choice of the opponent.
        opponent_choice = choice(choices)
        if opponent_choice == 'R':
            print(f"The opponent pick: {R}")
        elif opponent_choice == 'P':
            print(f"The opponent pick: {P}")
        elif opponent_choice == 'S':
            print(f"The opponent pick: {S}")
        
        # Deciding factors for the win, lose or tie.
        if player_choice == opponent_choice:
            print("Woah. It's a TIE!")
        elif player_choice == 'R' and opponent_choice == 'S':
            print("Nice! You WIN!")
        elif player_choice == 'P' and opponent_choice == 'R':
            print("Nice! You WIN!")
        elif player_choice == 'S' and opponent_choice == 'P':
            print("Nice! You WIN!")
        elif player_choice == 'R' and opponent_choice == 'P':
            print("Oops. You LOST.")
        elif player_choice == 'P' and opponent_choice == 'S':
            print("Oops. You LOST.")
        elif player_choice == 'S' and opponent_choice == 'R':
            print("Oops. You LOST.")
    
    # Error message for invalid inputs.
    else:
        print("Invalid choice. Please pick again from the given choices.")
        continue
        