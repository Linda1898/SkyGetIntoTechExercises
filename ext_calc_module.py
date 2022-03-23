import operator
def welcome_calc():
    print("""
    Welcome to Calculator! Enter a first set of numbers and then a second set. Then enter as many 
    operators as you would like (- * + / only!). To add more than one number or operator press enter and add another.
    To finish inputting a set of numbers or operators enter 'f'.
    
    The calculator will take the first set of numbers and depending on your choice of operators will either multiply, 
    divide, add or subtract using the second set of numbers.
    Enjoy!
    """)

def get_list_of_numbers_from_user():
    num=0
    num_list=[]
    while num != "f":
        num = input("Please enter a number: ")
        if num != "f":
            try:
                num = float(num)
                num_list.append(num)
            except ValueError:
                print("Only numbers will work!  ")
    return num_list

def get_list_of_operators_from_user():
    operator = 0
    operator_list = []
    while operator != "f":
        operator = input("Please enter an operator: ")
        if operator == "*" or operator == "/" or operator == "-" or operator == "+":
            operator_list.append(operator)
        else:
            if operator != "f":
                print("Only * / + - will work!")
    return operator_list


def print_result_and_return_file_content_to_save(first_nums,second_nums,operators):
    operator_dict = {}
    #declare dict as global variable - keep constants out of functions
    file_list = []
    for i in operators:
        if i == "*":
            operator_dict["*"] = operator.mul
        elif i == "/":
            operator_dict["/"] = operator.truediv
        elif i == "-":
            operator_dict["-"] = operator.sub
        elif i == "+":
            operator_dict["+"] = operator.add

    print("\n----------------------------------------------------------\n")
    print("\nAll possible answers are: \n")
    for i in first_nums:
        for j in second_nums:
            for k, v in operator_dict.items():
                if j == 0 and k == "/":
                    calcVar1 = f"Cannot perform {i} {k} {j} because you cannot divide by zero."
                    file_list.append(calcVar1)
                    print(calcVar1)
                    continue
                else:
                    calcVar2 = f"{i}{k}{j} =  {v(i, j)}"
                    file_list.append(calcVar2 + "\n")
                    print(calcVar2)
                    continue
    return file_list

def calc_save_result(content_to_be_saved):
    saveToFile = ""
    userFileName = 0
    while userFileName != "q":
        userFileName = input('Press q to quit or if you would like to save your work insert a file name. It must start with a letter, only use letters and numbers, and be no more than 15 characters long: ')
        if all([i.isalpha() or i.isdigit() for i in userFileName]) and userFileName[0].isalpha() and len(
                userFileName) <= 15 and userFileName != "q":
            try:
                fileCreated = open("%s.txt" % userFileName, "x")
                fileCreated.writelines(content_to_be_saved)
                fileCreated.close()
                break
            except FileExistsError:
                print("That file name exists already. Try again or press 'q' to quit.")
        else:
            if userFileName != "q":
                print("Try again or press 'q' to quit")