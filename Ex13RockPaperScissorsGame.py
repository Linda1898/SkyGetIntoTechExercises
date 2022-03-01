import random
play_again = 0
comp_input = 0
input_dict = {0: "rock", 1: "paper", 2: "scissors", "r": "rock", "p": "paper", "s": "scissors"}
user_input = ""
score_sheet=[0,0]
#TODO:How to work score sheet? global vs local variables is tricky.

def welcome_message():
    print("""
    Let\'s play Rock Paper Scissors!
    Remember rock beats scissors, scissors beats paper, and paper beats rock!
    Enter q to quit.
    """)

#TODO: check this without def to see why it's not working is it because it's within a variable?
# It accepts ints and chars but in the main script it does not
def check_user_input_is_str(input_from_user):
    try:
        input_from_user.isalpha()
        return True
    except AttributeError:
        print("Try again")


def play(player1, player2, scoreSheet):
    player1_wins_list = ["The computer wins! Muhahahahahaha.....", "You thought you could beat me?? Foolish mortal", "Dare to play again..."]
    player2_wins_list = ["Noooooooo", "How could this happen?", "I think you cheated"]
    if player1 == player2:
        print(f"It\'s a draw! You both played {player1}")
    elif player1 == "scissors" and player2 == "paper" or player1 == "rock" and player2 == "scissors" or player1 == "paper" and player2 == "rock":
        print(f"Ha! {player1} beats {player2}. {random.choice(player1_wins_list)}")
        scoreSheet[0] = scoreSheet[0]+1
    elif player2 == "scissors" and player1 == "paper" or player2 == "rock" and player1 == "scissors" or player2 == "paper" and player1 == "rock":
        print(f"Noooo {player2} beats {player1}. {random.choice(player2_wins_list)}")
        scoreSheet[1] = scoreSheet[1]+1



while play_again != "q" and user_input != "q":
    play_again = input("Would you like to start? Press 's' to start or 'q' to quit: ")
    # if play_again.isalpha(): works when in the string but when passed through the function it doesn't.
    if check_user_input_is_str(play_again):
        play_again = play_again.lower()
        while play_again == "s" and user_input != "q":
            welcome_message()
            while play_again == "s" and user_input != "q":
                user_input = input("Please enter 'r', 'p' or 's' for rock, paper, scissors: ")
                if check_user_input_is_str(user_input):
                    user_input = user_input.lower()
                    if user_input == "r" or user_input == "p" or user_input == "s":
                        user_input = input_dict[user_input]
                        comp_input = input_dict[random.randint(0, 2)]
                        play(comp_input, user_input, score_sheet)
                        print(f"Your scores are:\nComputer = {score_sheet[0]} Your score = {score_sheet[1]}")
                    elif user_input != "r" and user_input != "p" and user_input != "s" and user_input != "q":
                        print("Invalid Input, try again or enter 'q' to quit.")
                else:
                    print('Invalid input.')
    else:
        print('Invalid input.')

print('Until next time...')