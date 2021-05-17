# Rock Paper Scissors Game

# Computer randomly selects using random module
# Player if prompted to provide input and is compared to computers choice

import random

choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(choices)
player = False
computer_score = 0
player_score = 0

while True:
    player_choice = input(
        "Rock, Paper or Scissors? (Type 'End' to exit game)"
    ).capatalize()
    if player_choice == computer_choice:
        print("Tie")
    elif player == "Rock":
        if computer_choice == "Paper":
            print("You lose! ", computer_choice, " covers ", player_choice)
            computer_score += 1
        else:
            print("You win! ", player_choice, " crushes ", computer_choice)
            player_score += 1
    elif player_choice == "Scissors":
        if computer_choice == "Rock":
            print("You lose! ", computer_choice, " crushes ", player_choice)
            computer_score += 1
        else:
            print("You win! ", player_choice, " cuts ", computer_choice)
            player_score += 1
    elif player_choice == "Rock":
        if computer_choice == "Paper":
            print("You lose! ", computer_choice, " covers ", player_choice)
            computer_score += 1
        else:
            print("You win! ", player_choice, " crushes ", computer_choice)
            player_score += 1
    elif player_choice == "End":
        print("Final Scores:")
        print("Computer: ", computer_score)
        print("Player: ", player_score)
        break
    else:
        print("That's an invalid move")
    computer_choice = random.choice(choices)
