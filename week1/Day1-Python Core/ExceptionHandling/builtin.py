try:
    # This will cause ValueError
    x = int("8") 
    y = x/0
    
except ValueError:
    print("Not Valid!")
    
except ZeroDivisionError:
    print("Zero has no inverse!")

else:
    print("result is" , y)

a = ["10" , "tewnty" , 30]

try:
    ans = a[0] + a[2]
except ValueError:
    print("invalid conversion")
except TypeError:
    print("invalid type")  
else:
    print(ans)      

# to catch multiple exceptions in one

try:
    res = a[0] + a[2]
except (ValueError , TypeError) as e:
    print(f"error occur {e}")
else:
    print("execution completed")    

using raise keyword

def set_age(x):
    try:
        if(x<0):
            raise ValueError("Age cannot be negative")
    except ValueError as e: 
        print(e)    

set_age(-4)

# custom class and raising error by inheriting from Built in Exception class

class AgeError(Exception):
    pass


def age(x):
    try:
        if x < 0:
            raise AgeError("Age cannot be negative")
    except AgeError as e:
        print("error occur" , e)
age(-3)
b = dir(locals()['__builtins__'])
print(b)