# passing function to variavle
def show(x):
    print(x)

temp = show
temp(3)    

# pssing function as an argument
def myName(x):
    print(f"my name is {x}")

def getMyName(MyName , name):
    print("calling my name function")
    MyName(name)

getMyName(myName , "fareha")

# returning functions from the other function
def fun1(x):
    def func2():
        return x*2
    return func2
ans = fun1(3)
print(ans())
    
# storing function in a data structure
def add(a , b):
    return a+b
def subt(b , c):
    return a-b

m = {
    "add" : add,
    "subtract" : subt
}

addition = m["add"](5,3)
print(addition)

