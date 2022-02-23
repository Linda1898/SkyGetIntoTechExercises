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
fileList=[]
saveToFile = "a"
userFileName = 0
calcVar1 = 0
calcVar2 = 0
# TODO: ask Martina if this is good practice - to get rid of while true loop we put if num1 != q etc but the variables
#  were not defined until the while loop so this broke the code so have defined them as zero. Also had to add an if
#  statement before the try or it would accept f and q and try to float them.
# NOTE CHECKING BRANCH TO SEE DIFFERENCE

play = input("Press 's' to start or 'q' to quit: ")
while play == "s" and num1 != "q" and num2 != "q" and operator != "q":
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
        print("\nAll possible answers are: \n")
        for i in num1list:
            for j in num2list:
                for k, v in operatorDict.items():
                    if j == 0 and k == "/":
                        calcVar1 = f"Cannot perform {i} {k} {j} because you cannot divide by zero."
                        fileList.append(calcVar1)
                        print(calcVar1)
                        continue
                    else:
                        calcVar2 = f"{i}{k}{j} =  {v(i, j)}"
                        fileList.append(calcVar2 + "\n")
                        print(calcVar2)
                        continue

    while userFileName != "q":
        userFileName = input('Press q to quit or if you would like to save your work insert a file name. It must start with a letter, only use letters and numbers, and be no more than 15 characters long: ')
        if all([i.isalpha() or i.isdigit() for i in userFileName]) and userFileName[0].isalpha() and len(
                userFileName) <= 15 and userFileName != "q":
            try:
                fileCreated = open("%s.txt" % userFileName, "x")
                fileCreated.close()
                break
            except FileExistsError:
                print("That file name exists already. Try again or press 'q' to quit.")
        else:
            if userFileName != "q":
                print("Try again or press 'q' to quit")

    fileCreated = open("%s.txt" % userFileName, "w")
    fileCreated.writelines(fileList)
    fileCreated.close()
    print("\n---------------------------------------------------------------\n")
    play = input("Would you like to play again? Press 's' to start or 'q' to quit: ")
    if play == "s":
        num1 = 0
        num2 = 0
        operator = 0
        num1list = []
        num2list = []
        operatorDict = {}
        fileList = []
        saveToFile = "a"
        userFileName = 0
        calcVar1 = 0
        calcVar2 = 0

