import time

"""Part A """
def calculator(x , y , op ):
    ans = 0
    try: 
        if(op == "+"):
            ans = x + y
        elif(op == "-"):
            ans = x - y
        elif(op == "*"):
            ans = x * y
        elif(op == "/"):
            if y == 0:
                raise ZeroDivisionError("Invalid Input.Cannot divide by zero.")
            else:   
                ans = x // y  
        return ans   
    except ZeroDivisionError as e:
        return e
result = calculator(3 , 0, "/")
print(result)

""" Part B """

def summarise(*args , **kwargs):
    ans = sum(args)

    for key , val in kwargs:
        print(f"{key} = {val}")

"""Part C """
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(map(lambda  x : x*x , numbers))
print(result)

""" Part D"""
def timer(func):
    def wrapper(*args , **kwargs):
        start = time.time()
        ans = func(*args , **kwargs)
        end = time.time()
        print(f"Time taken {(end-start)*1000} ms")
    return wrapper

@timer
def sums():
    sum = 0 
    for i in range(1000001):
        sum+=i

sums()