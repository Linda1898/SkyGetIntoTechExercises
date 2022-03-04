import random

def welcome_message():
    print("""
    Let\'s play Rock Paper Scissors!
    Remember rock beats scissors, scissors beats paper, and paper beats rock!
    Are you ready?
    """)

def user_input():
    user_input_dict = {"r": "rock", "p": "paper", "s": "scissors"}
    user_input = ""
    while user_input != "q":
        user_input = input("Please enter 'r', 'p' or 's' for rock, paper, scissors: ")
        if user_input.isalpha():
            user_input = user_input.lower()
            if user_input == "r" or user_input == "s" or user_input == "p":
                user_input = user_input_dict[user_input]
                return user_input
            elif user_input != "q":
                print("Invalid input")
        else:
            print("Invalid input")



def computer_turn():
    input_dict = {0: "rock", 1: "paper", 2: "scissors"}
    computer = input_dict[random.randint(0, 2)]
    return computer

def play_game(computer,player1,scores):
    computer_wins_list = ["The computer wins! Muhahahahahaha.....", "You thought you could beat me?? Foolish mortal",
                         "Dare to play again..."]
    player1_wins_list = ["Why why why???", "How could this happen?", "I think you cheated"]

    if computer == player1:
        print(f"It\'s a draw! You both played {player1}")
    elif computer == "scissors" and player1 == "paper" or computer == "rock" and player1 == "scissors" or computer == "paper" and player1 == "rock":
        print(f"Ha! {computer} beats {player1}. {random.choice(computer_wins_list)}")
        scores[0] = scores[0] + 1
    elif player1 == "scissors" and computer == "paper" or player1 == "rock" and computer == "scissors" or player1 == "paper" and computer == "rock":
        print(f"Noooo {player1} beats {computer}. {random.choice(player1_wins_list)}")
        scores[1] = scores[1] + 1
    print(f"Your scores are:\n Computer {scores[0]} You: {scores[1]}")