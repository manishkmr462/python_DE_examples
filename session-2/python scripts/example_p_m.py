import package_example.module_1 as m1
import package_example.module_2 as m2

choice = int(input("""Enter a choice:
                   1. list of only numbers seperated by comma
                   2. list of only strings seperated by comma"""))
inp_list = []
if choice == 1:
    inp = input("Enter list of only numbers seperated by comma")
    inp_list = [float(x) for x in inp.split(',')]
    print(f"Sum of all the numbers are: {m1.add_all_numbers(inp_list)}")
elif choice == 2:
    inp = input("Enter list of only strings seperated by comma")
    inp_list = inp.split(',')
    choice = int(input("""Enter the choice:
                       1. Capitalize all the strings
                       2. make all of them upper case"""))
    if choice == 1:
        print(m2.capitalize_all_strs(inp_list))
    elif choice == 2:
        print(m2.upper_case_all_strs(inp_list))

