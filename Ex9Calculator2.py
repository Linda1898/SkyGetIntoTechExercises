num1List = []
num2List = []

def PlayAgain():
    print("\n\nRemember when asked for an operator just press q to quit \n")
    while True:
        num1 = input( "Please enter a number, if you would like to add more than one number press enter and add another, press 'f' to finish: ")
        if num1 != 'f':
            try:
                num1=float(num1)
                num1list.append(num1)
                break
            except  ValueError:
                print("Only numbers will work!  ")
                continue
        elif num1 == 'f':
            break


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
        PlayAgain()
    elif operator == "-":
        print("The result is ", num1 - num2)
        PlayAgain()
    elif operator == "*":
        print("The result is ", num1 * num2)
        PlayAgain()
    elif operator == "/":
        print("The result is ", num1 / num2)
        PlayAgain()


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
    PlayAgain()
elif operator == "-":
    print ("The result is ", num1 - num2)
    PlayAgain()
elif operator == "*":
    print("The result is ", num1 * num2)
    PlayAgain()
elif operator == "/" and num2 != 0:
    print("The result is ", num1 / num2)
    PlayAgain()
elif operator == "/" and num2 == 0:
    while True:
        try:
            print("The result is ", num1 / num2)
            PlayAgain()
        except ZeroDivisionError:
            print('You cannot divide by zero')
            PlayAgain()

        # TODO: Fix this bug it doesn't work when doing the zero division twice, only once!