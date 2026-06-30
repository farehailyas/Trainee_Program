import math


# local variable test
def fun():
    x = 100
    print(f"inside function value is {x}")

# outside function acessing x will give error
# print(x) #this will give an error

# global variable
history = []
# calculations
def apply_operation(func , *args , **kwargs):
    ans = func(*args,**kwargs)
    history.append(ans)
    return ans

# operations
# 1- add
def add(*args):
    return sum(args)
# 2- multiply
def multiply(*args):
    return math.prod(args)
# 3- describe
def describe(**kwargs):
    description = ""
    for key , val in kwargs.items():
        description += f"{key} = {val} ,"
    return description[:-1]

# functions toolkit
get_sum = apply_operation(add, 2,3,4,5,6,7,8,9)
get_mul = apply_operation(multiply, 2,3,9,4,3,5,7)
get_desc = apply_operation(describe , name = "Calculator" , version = 1.1 )

# print(get_sum)
# print(get_mul)
# print(get_desc)
print(f"Operation History {history}")