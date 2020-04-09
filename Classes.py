from functools import reduce

# First task
class Boss:
    def __init__(self, number):
        self.number = number

    def __del__(self):
        print("You deleted class object")

    def is_divisible_by(self, divisor):
        return self.number % divisor == 0

    @staticmethod
    def multiple(num_1, num_2):
        mult_func = lambda num_1 , num_2: num_1 * num_2
        return mult_func(num_1, num_2)


boss = Boss(5)
print(boss.is_divisible_by(3))
print(Boss.multiple(2, 7))
print(boss.multiple(2, 7))


# Second task
class JuniorBoss(Boss):
    __protected_var = 17
    def __is_object_string(self, object):
        return type(object) == type('')


junior = JuniorBoss(3)
print(junior.multiple(2, 7))
print(junior._JuniorBoss__is_object_string(8))
print(junior._JuniorBoss__protected_var)


# Third task
class LittleBoss(JuniorBoss):
    @staticmethod
    def multiple(num_1, num_2):
        nok = num_1 * num_2
        while num_1 != 0 and num_2 != 0:
            if num_1 > num_2:
                num_1 %= num_2
            else:
                num_2 %= num_1
        nod = num_2 + num_1
        nok /= nod

        return nok, nod

little = LittleBoss(8)
print(little.multiple(67, 54))


# Fourth task

# Use map to print the square of each numbers rounded
# to two decimal places
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.
map_result = list(map(lambda x: round(x**2, 2), my_floats))
filter_result = list(filter(lambda name: len(name) <= 7, my_names))
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)
