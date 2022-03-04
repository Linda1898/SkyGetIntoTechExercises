import RPSModule
play_again = 0
score_sheet=[0,0]

RPSModule.welcome_message()
play_again = input("Enter 's' to start or 'q' to quit: ")
while play_again != "q":
    if  play_again == "s" or play_again == "y":
        player = RPSModule.user_input()
        comp = RPSModule.computer_turn()
        RPSModule.play_game(comp, player, score_sheet)
        play_again = input("would you like to play again? enter 'y' for yes or 'q' to quit: ")
    elif play_again != "q":
        print("Invalid input")
        play_again = input("Enter 's' to start or 'q' to quit: ")
print('Until next time...')


