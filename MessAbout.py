num1list = []
num2list = []
operatorDict = {}
m = operator.mul
d = operator.truediv
s = operator.sub
a = operator.add



def PlayAgain():


    print("""
    Hi I am a calculator!
    To quit press q then enter.
    To add more than one number or operator press enter and add another.
    To finish inputting numbers press 'f' and enter.
    """)
    while True:
        num1 = input("Please enter a number: ")
        if num1 != "f" and num1 != "q":
            try:
                num1 = float(num1)
                num1list.append(num1)
                continue
            except ValueError:
                print("Only numbers will work!  ")
                continue
        elif num1 == "f":
            print('Thank you')
            break
        elif num1 == "q":
            print('Goodbye')
            break

    while True:
        if num1 == "q":
            break
        num2 = input("Please enter a number: ")
        if num2 != "f" and num2 != "q":
            try:
                num2 = float(num2)
                num2list.append(num2)
                continue
            except ValueError:
                print("Only numbers will work!  ")
                continue
        elif num2 == "f":
            print('Thank you')
            break
        elif num2 == "q":
            print("Goodbye")
            break

    while True:
        if num1 == "q" or num2 == "q":
            break
        operator = input("Please enter an operator (use * / + - only) and press enter: ")
        if operator != "*" and operator != "/" and operator != "-" and operator != "+" and operator != "q" and operator != "f":
            continue
        elif operator == "*":
            operatorDict["*"] = m
            continue
        elif operator == "/":
            operatorDict["/"] = d
            continue
        elif operator == "-":
            operatorDict["-"] = s
            continue
        elif operator == "+":
            operatorDict["+"] = a
            continue
        elif operator == "f":
            print("Thank you")
            break
        elif operator == "q":
            print("Goodbye")
            break

    if num1 != "q" and num2 != "q" and operator != "q":
        print("\n----------------------------------------------------------\n")
        print("\nAll possible answers are: ")
        for i in num1list:
            for j in num2list:
                for k, v in operatorDict.items():
                    if j == 0 and k == "/":
                        print("Cannot perform", i, k, j, "because you cannot divide by zero.")
                        continue
                    else:
                        print(i, k, j, " = ", v(i, j))

while True:
    Play = input('Would you like to play again? press y to play and n to quit: ')
    if Play.lower() == 'y':
        PlayAgain()
    elif Play.lower() == 'n':
        break
    else:
        print('Please press y to play again or n to quit')

