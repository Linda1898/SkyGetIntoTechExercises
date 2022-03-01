def play_again():
    print("\n\nRemember when asked for an operator just press q to quit \n")
    while True:
        try:
            num1 = float(input("Please enter a number: "))
            break
        except  ValueError:
            print("Only a number will work!  ")
            continue

    while True:
        try:
            num2 = float(input("Please enter another number: "))
            break
        except  ValueError:
            print("Only a number will work! ")
            continue

    operator = input("please enter an operator (use * / + - only): ")
    while operator != "*" and operator != "/" and operator != "-" and operator != "+" and operator != "q":
        operator = input("please enter an operator (use * / + - only): ")

    if operator == "q":
        print('Goodbye')
    elif operator == "+":
        print("The result is", num1 + num2)
        play_again()
    elif operator == "-":
        print("The result is ", num1 - num2)
        play_again()
    elif operator == "*":
        print("The result is ", num1 * num2)
        play_again()
    elif operator == "/":
        print("The result is ", num1 / num2)
        play_again()


print("Welcome to my calculator! \n\nTo quit the programme: enter q when asked for an operator\n")
while True:
    try:
        num1 = float(input("Please enter a number: "))
        break
    except  ValueError:
        print("Only a number will work! ")

while True:
    try:
        num2 = float(input("Please enter another number: "))
        break
    except  ValueError:
        print("Only a number will work! ")
        continue

operator = input("please enter an operator (use * / + - only): ")
while operator != "*" and operator != "/" and operator != "-" and operator != "+" and operator != "q":
    operator = input("please enter an operator (use * / + - only): ")

if operator == "q":
    print('Goodbye')
elif operator == "+":
    print ("The result is", num1 + num2)
    play_again()
elif operator == "-":
    print ("The result is ", num1 - num2)
    play_again()
elif operator == "*":
    print("The result is ", num1 * num2)
    play_again()
elif operator == "/" and num2 != 0:
    print("The result is ", num1 / num2)
    play_again()
elif operator == "/" and num2 == 0:
    try:
        print("The result is ", num1 / num2)
        play_again()
    except ZeroDivisionError:
        print('You cannot divide by zero')
        play_again()
        # TODO: Fix this bug it doesn't work when doing the zero division twice, only once!