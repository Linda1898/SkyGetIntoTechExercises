import random
playAgain = 0
compInput = 0
InputDict = {0: "rock", 1: "paper", 2: "scissors", "r": "rock", "p": "paper", "s": "scissors"}
userInput = "a"


def welcome_message():
    print("""
    Let\'s play Rock Paper Scissors!
    Remember rock beats scissors, scissors beats paper, and paper beats rock!
    Enter q to quit.
    """)


def check_user_input_is_str(input_from_user):
    try:
        input_from_user.lower()
        print('it\'s a string')
        return True
    except AttributeError:
        print("Try again")


def play(player1, player2):
    player1_score = 0
    player2_score = 0
    player1_wins_list = ["The computer wins! Muhahahahahaha.....", "You thought you could beat me?? Foolish mortal", "Dare to play again..."]
    player2_wins_list = ["Noooooooo", "How could this happen?", "I think you cheated"]
    if player1 == player2:
        print(f"It\'s a draw! You both played {player1}")
    elif player1 == "scissors" and player2 == "paper" or player1 == "rock" and player2 == "scissors" or player1 == "paper" and player2 == "rock":
        print(f"Ha! {player1} beats {player2}. {random.choice(player1_wins_list)}")
        player1_score += 1
    elif player2 == "scissors" and player1 == "paper" or player2 == "rock" and player1 == "scissors" or player2 == "paper" and player1 == "rock":
        print(f"Noooo {player2} beats {player1}. {random.choice(player2_wins_list)}")
        player2_score += 1
    print(f"Your scores are:\nComputer = {player1_score} Your score = {player2_score}")


while playAgain != "q":
    playAgain = input('Would you like to play? ')
    if check_user_input_is_str(playAgain):
        playAgain = playAgain.lower()
        if playAgain == "y":
            break
        else:
            print('You can only enter y to play or enter q to quit: ')


while playAgain == "y" and userInput != "q":
    welcome_message()
    while playAgain == "y" and userInput != "q":
        userInput = input('Please enter r p s for rock paper scissors: ')
        if check_user_input_is_str(userInput):
            userInput = userInput.lower()
            if userInput == "r" or userInput == "p" or userInput == "s":
                userInput = InputDict[userInput]
                compInput = InputDict[random.randint(0, 2)]
                play(compInput, userInput)
                playAgain = input('Would you like to play again? ')
            else:
                print("You can only enter r p or s or enter q to quit:")



print("Until next time...")