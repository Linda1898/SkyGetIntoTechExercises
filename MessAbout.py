# right click on the numbers downt he left to get red dot to execute code there when run
#click green bug to whats happening

import operator
num1list = []
num2list = []
operatorDict = {}
m = operator.mul
d = operator.truediv
s = operator.sub
a = operator.add
num1 = 0
num2 = 0
operator = 0

Play = input("Press 's' to start or 'q' to quit: ")
while Play == "s" and num1 != "q" and num2 != "q" and operator != "q" :
    print("""
            Hi I am a calculator!
            To quit press 'q' then enter.
            To add more than one number or operator press enter and add another.
            To finish inputting numbers press 'f' and enter.
            """)
    while num1 != "f" and num1 != "q":
        num1 = input("Please enter a number: ")
        if num1 != "f" and num1 != "q":
            try:
                num1 = float(num1)
                num1list.append(num1)
                continue
            except ValueError:
                print("Only numbers will work!  ")
                continue

    while num2 != "f" and num2 != "q" and num1 != "q":
        num2 = input("Please enter another number: ")
        if num2 != "f" and num2 != "q":
            try:
                num2 = float(num2)
                num2list.append(num2)
                continue
            except ValueError:
                print("Only numbers will work! ")
                continue

    while num1 != "q" and num2 != "q" and operator != "q" and operator != "f":
        operator = input("Please enter an operator: ")
        if operator != "*" and operator != "/" and operator != "-" and operator != "+" and operator != "q" and operator != "f":
            print("Only * / + - will work!")
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

        print("\n---------------------------------------------------------------\n")
        Play = input("Would you like to play again? Press 's' to start or 'q' to quit: ")
        if Play == "s":
            num1 = 0
            num2 = 0
            operator = 0
            num1list = []
            num2list = []
            operatorDict = {}


