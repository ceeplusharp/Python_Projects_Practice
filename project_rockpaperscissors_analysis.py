# A simple take on the Rock, Paper, Scissors game.
# Just using if-elif-else statements and while loop.
# Additional summary showing percentages for win, lose and tie.

from random import choice

# Initialize variables for game summary computations.
total_games = 0
total_win = 0
total_lose = 0
total_tie = 0

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
    
    # Deciding factors for the win, lose or tie.
    # Simple print functions to display the choice of the user.
    if player_choice in choices:
        total_games += 1
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
            total_tie += 1
        elif player_choice == 'R' and opponent_choice == 'S':
            print("Nice! You WIN!")
            total_win += 1
        elif player_choice == 'P' and opponent_choice == 'R':
            print("Nice! You WIN!")
            total_win += 1
        elif player_choice == 'S' and opponent_choice == 'P':
            print("Nice! You WIN!")
            total_win += 1
        elif player_choice == 'R' and opponent_choice == 'P':
            print("Oops. You LOST.")
            total_lose += 1
        elif player_choice == 'P' and opponent_choice == 'S':
            print("Oops. You LOST.")
            total_lose += 1
        elif player_choice == 'S' and opponent_choice == 'R':
            print("Oops. You LOST.")
            total_lose += 1
    
    # Prompt for the program to quit when the user decides to.
    elif player_choice == 'q':
        if total_games == 0:
            print("Thank you for playing!\n")
            break
        else:
            # Game summary computations.
            percentage_win = (total_win / total_games) * 100
            percentage_lose = (total_lose / total_games) * 100
            percentage_tie = (total_tie / total_games) * 100
            print("Thank you for playing!\n\n"
                "***Summary of Games Played***\n"
                f"Total Number of Games Played: {total_games}\n"
                f"% Win: {percentage_win:.2f} %\n"
                f"% Lose: {percentage_lose:.2f} %\n"
                f"% Tie: {percentage_tie:.2f} %\n"
                "***Nothing follows.***\n")
            break
    
    # Error message for invalid inputs.
    else:
        print("Invalid choice. Please pick again from the given choices.")
        continue
    