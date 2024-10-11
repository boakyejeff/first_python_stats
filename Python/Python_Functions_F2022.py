# %%
def greeting():
    """Simple greeting message"""
    print("Hello user...")

# %%
greeting()

# %%
def greeting(name):
    """Fancy greeting message"""
    print(f"Say hello to {name.title()}, Python.")
    print(f"Hello {name.title()}...")

# %%
greeting("john")

# %%
def add_two_numbers(a, b):
    """This function adds the numbers a and b together"""
    answer = a + b**2
    return answer

# %%
# 1 + 2^2 = 5
add_two_numbers(1, 2)

# %%
# 2 + 1^2 = 3
add_two_numbers(2, 1)

# %%
def add_two_numbers(a, b = 10):
    """This function adds the numbers a and b together"""
    answer = a + b**2
    return answer

# %%
add_two_numbers(10) # 10 + 10^2 = 110

# %%
add_two_numbers(10, 4)  # 10 + 4^2 = 26

# %%
def hello_user(FirstName, LastName, MiddleName=""):
    """Greets the user, with middlename OPTIONAL"""
    # Empty strings will evaluate to False
    if MiddleName:
        print(f"Hello {FirstName} {MiddleName} {LastName}")
    else:
        print(f"Hello {FirstName} {LastName}")


# %%
hello_user("John","Snyder")

# %%
hello_user("James","McCartney","Paul")

# %%
def add_two_numbers(a, b = 10, c = ""):
    """This function adds the numbers a, b,
       as well as c together"""

    if c: return a + b**2 + c
    else: return a + b**2


# %%
add_two_numbers(a = 10, b = 4)  # 10 + 4^2 = 26

# %%
add_two_numbers(a = 10, b = 4, c = 5)  # 10 + 4^2 + 5 = 31

# %%
#                      Input a List
def SortedTitleCaseString(str_list):
    # Sort list of strings
    str_list.sort()
    # return a list comprehension
    ret_list = [x.title() for x in str_list]
    return ret_list


# %%
names = ["john","zach","jim","bill"]

# %%
ret = SortedTitleCaseString(names)


# %%
def my_print_function(a_string):
    print(f"I am going to print the string now:\n{a_string}")


# %%
my_print_function("Hello")


# %%
result = my_print_function("Hello")

# result not printed by interpreter!
print(result)
bool(result)


# %%
def times_2(x):
    return 2*x

# %%
def times_3(x):
    return 3*x

# %%
def do_operation(fun, x):
    return fun(x)

# %%
do_operation(times_2, 4)

# %%
do_operation(times_3, 4)

# %%
do_operation(times_3, times_2(5))

# %%
def append_one(a_list):
    """This appends 1 to the list we pass"""
    a_list.append(1)

# %%
a_list = [4,3,2]

# %%
print(a_list)

# %%
append_one(a_list)

# %%
print(a_list)


# %%
glob_var = 1 # This is global variable.
def add_numbers(a, b):
    result = a + b + glob_var
    return result

# %%
add_numbers(1, 1)

# %%
print(a) #not available outside add_numbers()


import LibsAndFunctions


# %%
square_all(1, 2, 3)

# %%
add_abc(2, 2, 2)

# %%
def square_all(a, b, c):
    return a**2, b**2, c**2

# %%
list(square_all(2,3,4))

# %%
do_operation(lambda x: x**(0.5), 4)

# %%
lambda x: x**(0.5)

# %%
def my_sqrt(x):
    return x**(0.5)
