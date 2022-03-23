import operator
import ext_calc_module

play = input("Press 's' to start or 'q' to quit: ")
while play == "s":
    ext_calc_module.welcome_calc()
    print('Please enter your first set of numbers.')
    list_nums1 = ext_calc_module.get_list_of_numbers_from_user()
    print('Now enter your second set of numbers.')
    list_nums2 = ext_calc_module.get_list_of_numbers_from_user()
    list_operators = ext_calc_module.get_list_of_operators_from_user()
    file_content = ext_calc_module.print_result_and_return_file_content_to_save(list_nums1, list_nums2, list_operators)
    ext_calc_module.calc_save_result(file_content)
    print("\n---------------------------------------------------------------\n")
    play = input("Would you like to play again? Press 's' to start or 'q' to quit: ")

