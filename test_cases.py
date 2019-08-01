from pandas import DataFrame
from any_iter import any_iter

def print_test(prompt, arg, _exit="\n\n"):
    print(prompt,"returns", any_iter(arg), end=_exit)

def test():
    empty_data_frame = DataFrame([])
    full_data_frame = DataFrame([1,2,3,4,5])
    empty_list = []
    full_list = [1,2,3,4,5]
    empty_list_of_lists = [[], []]
    false_list_of_lists = [[False, False], [False, False, False]]
    true_list_of_lists = [[False, False], [False, True, False]]
    false_list = [False, False]
    true_list = [False, True]
    empty_dict = {}
    normal_dict = {"Cat": 14}
    false_dict = {False: True}
    true_dict = {True: False}
    

    print_test("Empty data frame", empty_data_frame)
    print_test("Full data frame", full_data_frame)
    print_test("Empty list", empty_list)
    print_test("Full list", full_list)
    print_test("Empty list of lists", empty_list_of_lists)
    print_test("False list of lists", false_list_of_lists, " ")
    print("because at least one list is populated\n")
    print_test("True list of lists", true_list_of_lists)
    print_test("False list", false_list)
    print_test("Normal dict", normal_dict)
    print_test("False dict", false_dict)
    print_test("True dict", true_dict)
    print_test("True", True)
    print_test("False", False)
    print_test("0", 0)
    print_test("0.6", 0.6)
    print_test("'Cat'", 'Cat')
    
    test()
