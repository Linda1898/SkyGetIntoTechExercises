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
    num = "0"
    num_list = []
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
    op = "0"
    operator_dict = {}
    while op != "f":
        op = input("Please enter an operator: ")
        if op == "*":
            operator_dict["*"] = operator.mul
        elif op == "/":
            operator_dict["/"] = operator.truediv
        elif op == "-":
            operator_dict["-"] = operator.sub
        elif op == "+":
            operator_dict["+"] = operator.add
        else:
            if op != "f":
                print("Only * / + - will work!")
    return operator_dict


def print_result_and_return_file_content_to_save(first_nums, second_nums, operators):
    file_list = []
    print("\n----------------------------------------------------------\n")
    print("\nAll possible answers are: \n")
    for i in first_nums:
        for j in second_nums:
            for k, v in operators.items():
                if j == 0 and k == "/":
                    calc_var_1 = f"Cannot perform {i} {k} {j} because you cannot divide by zero."
                    file_list.append(calc_var_1)
                    print(calc_var_1)
                    continue
                else:
                    calc_var_2 = f"{i}{k}{j} =  {v(i, j)}"
                    file_list.append(calc_var_2 + "\n")
                    print(calc_var_2)
                    continue
    return file_list


def calc_save_result(content_to_be_saved):
    user_file_name = "0"
    while user_file_name != "q":
        user_file_name = input("""
                                Press q to quit or if you would like to save your work insert a file name. It must
                                start with a letter, only use letters and numbers, and be no more than 15 characters
                                long: 
                               """)
        if all([i.isalpha() or i.isdigit() for i in user_file_name]) and user_file_name[0].isalpha() and len(
                user_file_name) <= 15 and user_file_name != "q":
            try:
                file_created = open("%s.txt" % user_file_name, "x")
                file_created.writelines(content_to_be_saved)
                file_created.close()
                break
            except FileExistsError:
                print("That file name exists already. Try again or press 'q' to quit.")
        else:
            if user_file_name != "q":
                print("Try again or press 'q' to quit")
