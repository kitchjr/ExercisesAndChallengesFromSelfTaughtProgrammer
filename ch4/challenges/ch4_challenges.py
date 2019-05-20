# 1. Write a function that takes a number as an input and returns that number squared
def squared():
    """
    returns n**2
    :return: square of n
    """
    n = input("Type a number to square")
    n = int(n)
    return n**2

# 2. Create a function that accepts a string as a parameter and prints it
if __name__ == '__main__':
    def str_print(str_text: object) -> object:
        print(str_text)

str_print('booger')

# 3. Write a function that takes three required parameters and two optional parameters
def do_math(int1, int2, int3, exp1=2, exp2=3):
    """
    returns int1 * int2**exp1 + int3**exp2
    :param int1: int.
    :param int2: int.
    :param exp1: int
    :param exp2: int
    :return: int product and sum

    """
    return int1 * int2**exp1 + int3**exp2

print(do_math(2,3,4))

# Write a program with two (2) functions. The first function should take an integer as a parameter
# and return the result of that integer divided by 2. The second function should take an integer
# as a parameter and return the result of the integer multiplied by 4. Call the first function, save
# the result as a variable and pass it as a parameter to the second function.

def divide_by_two(an_int):
    """
    returns an_int / 2
    :param an_int: int.
    :return: int quotient of an_int divided by 2
    """
    return an_int / 2

def mult_by_four(an_int):
    """
    returns an_int * 4
    :param an_int: int.
    :return:
    """
    # make sure we're using an integer
    return int(an_int) * 4

pass_me = divide_by_two(10)

print(mult_by_four(pass_me))

# 5. Write a function that converts a string to a float and returns the result. Use exception handling

def str_to_float(string):
    """
    Converts a string to a float and returns that object as a float
    :param string: str.
    :return: float(string)
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert string to float")

my_num = str_to_float("66.6")
print(my_num)
