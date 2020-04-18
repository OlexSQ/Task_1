def from_task_2():
    var_integer = 28

    var_string = "This is a test string for Internship Onix for Python"

    if type(var_integer) == type(var_string):
        print("Are you crazy?")
    else:
        print("Type of var_integer is %s, and type of var_string is %s" % (type(var_integer), type(var_string)))

    var_integer = str(var_integer)
    print("Type of var_integer now is %s" % (type(var_integer)))

    new_list = [.0, 1.1, 2.22, 3.333, 4.4444]
    print(new_list)

    new_list.append(5.55555)
    print(new_list)

    new_list.insert(1, 6.666666)
    print(new_list)

    new_list.pop(0)
    print(new_list)

    del new_list[2]
    print(new_list)

    new_list.reverse()
    print(new_list)

    print("The quontity of elenements in my list is %d" % new_list.__len__())

    copy_of_new_list = list(new_list)  # Fixed
    print(type(copy_of_new_list))

    def sortMyList(my_list):
        sorter = True
        while sorter:
            sorter = False
            for index in range(my_list.__len__() - 1):
                if my_list[index] > my_list[index + 1]:
                    helper = my_list[index + 1]
                    my_list[index + 1] = my_list[index]
                    my_list[index] = helper
                    sorter = True
        return my_list

    my_sorted_list = sortMyList(copy_of_new_list)
    print(my_sorted_list)

    sorted_list_by_program = sorted(new_list)
    print(sorted_list_by_program)

    var_string = var_string.lower()
    var_string = var_string.split()
    sorted_string = sorted(var_string)
    print(sorted_string)

    price_list = {"Milk": 1.25, "Bread": 0.75, "Eggs": 0.55}
    print(price_list)

    price_list["Sugar"] = 0.68
    print(price_list)

    print("Price of the milk is %f $" % price_list["Milk"])

    price_list.pop("Bread")
    print(price_list)

    print(price_list.keys())

    print(price_list.values())

    sorted_dict_by_kyes = sorted(price_list.keys())
    print(sorted_dict_by_kyes)

    sortsd_dict_by_values = sorted(price_list.values())
    print(sortsd_dict_by_values)

global_var = 17

def multiple_numbers_and_return_list(number):
    func_list = [number * global_var]
    return func_list, len(func_list)

def print_all_args(*args, **kwargs):           # Changed names of arguments
    print(f"Args = {args}\nKwargs = {kwargs}")

def fibonacci_numders(quantity):
    if quantity == 1:
        return 0
    elif quantity == 2:
        return 1
    else:
        return fibonacci_numders(quantity - 1) + fibonacci_numders(quantity - 2)


if __name__ == '__main__':
    print(multiple_numbers_and_return_list(4))
    print_all_args("arg_1", "arg_2", kwarg_1=12, kwarg_2=167, kwarg_3 = 1000)
    print(fibonacci_numders(10))