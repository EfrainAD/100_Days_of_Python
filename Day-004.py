import random

choices = ["Rock", "Paper", "Scissor"]
def player_won():
    print("You Win!")
def computer_won():
    print("You Lose!")

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

print("You:", choices[player_choice])
print("Computer:",choices[computer_choice])

if player_choice == computer_choice:
    print("DRAW")
elif player_choice == 0:
    if computer_choice == 2:
        player_won()
    else:
        computer_won()
elif player_choice == 1:
    if computer_choice == 0:
        player_won()
    else:
        computer_won()
elif player_choice == 2:
    if computer_choice == 1:
        player_won()
    else:
        computer_won()
