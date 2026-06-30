# function decorator
# to have additional functionality on arguments after calling the function
def my_decorator(fun):
    def wrapper():
        print("before calling")
        fun()
        print("after calling")
    return wrapper

@my_decorator
def actualFunc():
    print("in the actual function")
actualFunc()

# class decorator
# to add parameters in the class in a decorator
def class_decorator(cls):
    cls.description = "testing class decorator" 
    return cls

@class_decorator
class abc:
    pass

print(abc.description)