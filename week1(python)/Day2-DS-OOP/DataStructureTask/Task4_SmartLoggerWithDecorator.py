
def log_call(func):
    def wrapper(*args , **kwargs):
        function_name = func.__name__ 
        print(f"[LOG] {function_name} called with args = {args}")
        ans = func(*args , **kwargs)
        print(f"[LOG] Result of {function_name}({args[0]}) : {ans}")
        return ans
    return wrapper

def add(*args):
    ans = sum(args)
    return ans
decor = log_call
decor(add)
ans = add(2,3,4)
print(ans)

# factorial
@log_call
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
  
# fibbonacci
@log_call
def fibonacci(n):
    if n==1 or n==0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter value to calculate factorial and fibonacci : "))
# caller
print(f"Calling factorial({n})")
res = factorial(n)
print(f"Result: {res}")
print("--------------")
print(f"Calling fibonacci({n})")
res = fibonacci(n)
print(f"Result: {res}")



# logging functionality is at one place
# if i use a simple logging function i might forget to call it in recursive one
# separation of business and auth,logging etc logic in it
# provide scalability .if i dont want logging later. have to remove function calls or code manually from the function 