import operator
num1list = []
num2list = []
operatorDict = {}
m = operator.mul
d = operator.truediv
s = operator.sub
a = operator.add
# TODO: ask Martina if this is good practice - to get rid of while true loop we put if num1 != q etc but the variables
#  were not defined until the while loop which broke the code so have defined them as zero below
num1 =0
num2 =0


print("""
Hi I am a calculator!
To quit press q then enter.
To add more than one number or operator press enter and add another.
To finish inputting numbers press 'f' and enter.
""")


while num1 != "f" or num1 != "q":
    num1 = input("Please enter a number: ")
    try:
        num1 = float(num1)
        num1list.append(num1)
        continue
    except ValueError:
        print("Only numbers will work!  ")
        continue

while num2 != "f" and num2 != "q"and num1 != "q":
    num2 = input("Please enter a number: ")
    try:
        num2 = float(num2)
        num2list.append(num2)
        continue
    except ValueError:
        print("Only numbers will work!  ")
        continue


while num1 != "q" or num2 !="q" or operator !="q":
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


if num1 != "q" and num2 != "q" and operator != "q":
    print("\n----------------------------------------------------------\n")
    print("\nAll possible answers are: ")
    for i in num1list:
        for j in num2list:
            for k,v in operatorDict.items():
                if j == 0 and k == "/":
                    print("Cannot perform", i, k, j, "because you cannot divide by zero.")
                    continue
                else:
                    print(i, k, j, " = ", v(i, j))


# reconsider your while true loops - put a condition in the while loop - safer and cleaner