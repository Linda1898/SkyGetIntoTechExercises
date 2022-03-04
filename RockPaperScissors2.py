# 1 welcome msg etc 2. user choice ask and convert 3. comp choice everything to do with that 4. logic of game
import random
play_again = 0
comp_input = 0
input_dict = {0: "rock", 1: "paper", 2: "scissors", "r": "rock", "p": "paper", "s": "scissors"}
user_input = ""
score_sheet=[0,0]

def check_user_input():
    user_input = input("Enter here: ")
    if user_input.isalpha():
       user_input = user_input.lower()
       return user_input  
    else:
        print("Invalid input function")


def convert_player_actions_to_RPS_variables(player1):
    player_variables = []
    while player1 != "q":
        if player1 == "r" or player1 == "p" or player1 == "s":
            player1 = input_dict[player1]
            computer = input_dict[random.randint(0, 2)]
            player_variables.append(computer)
            player_variables.append(player1)
        else:
            pass
    return player_variables

def play_game(computer,player1,):
    computer_wins_list = ["The computer wins! Muhahahahahaha.....", "You thought you could beat me?? Foolish mortal",
                         "Dare to play again..."]
    player1_wins_list = ["Noooooooo", "How could this happen?", "I think you cheated"]

    if computer == player1:
        print(f"It\'s a draw! You both played {player1}")
    elif computer == "scissors" and player1 == "paper" or computer == "rock" and player1 == "scissors" or computer == "paper" and player1 == "rock":
        print(f"Ha! {computer} beats {player1}. {random.choice(computer_wins_list)}")
        # scores[0] = scores[0] + 1
    elif player1 == "scissors" and computer == "paper" or player1 == "rock" and computer == "scissors" or player1 == "paper" and computer == "rock":
        print(f"Noooo {player1} beats {computer}. {random.choice(player1_wins_list)}")

        # scores[1] = scores[1] + 1
    # print(f"Your scores are:\nComputer = {score_sheet[0]} Your score = {score_sheet[1]}")



print("""
Let\'s play Rock Paper Scissors!
Remember rock beats scissors, scissors beats paper, and paper beats rock!
""")

print("Would you like to play? Enter y for yes or q to quit.")
play_again = check_user_input()
while play_again != "y" and play_again != "q":
    print("Invalid input - only 'y' or 'q' are accepted")
    play_again = check_user_input()

while play_again == "y" and user_input != "q":
    print("Please enter 'r', 'p' or 's' for rock, paper, scissors: ")
    user_input = check_user_input()
    player_actions = convert_player_actions_to_RPS_variables(user_input)
    play_game(player_actions[0],player_actions[1], score_sheet)
    print('Until next time...')