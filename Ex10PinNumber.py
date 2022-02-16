import getpass
attempts = 3

while attempts > 0:
    user_input=getpass.getpass(prompt='Please enter your pin number and press enter: ',)
    try:
        user_input=int(user_input)
    except ValueError:
        print("Please use numbers only")
        user_input = getpass.getpass(prompt='Please enter your pin number and press enter: ', )
    if user_input == 1234:
        print('Correct pin entered.')
        break
    elif user_input != 1234:
        attempts -= 1
        if attempts > 0:
            print('Incorrect pin entered, you have', attempts, " attempts left")
        elif attempts == 0:
            print('Pin entered incorrectly too many times, account blocked')

