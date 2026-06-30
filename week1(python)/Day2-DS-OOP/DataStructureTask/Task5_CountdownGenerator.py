def track_yields(func):
    def wrapper(*args , ** kwargs):
        function_name = func.__name__
        for result in func(*args , **kwargs):
            print(f"[TRACK] YIELDING {result}")
            yield result
    return wrapper

def countdown(n):
    i = n
    while i>0 :
        yield i
        i-=1
    yield "Go!"
@track_yields
def even_filter(numbers):
    x = (x for x in numbers if x%2 == 0)
    return x

@track_yields
def fibonacci_gen(limit):
    if limit == 0 :
        yield 0
    first = 0 
    second = 1
    for i in range(limit):
        if i == 0 or i == 1:
            yield i
        fib = first+second
        first = second
        second = fib
        yield fib

def helper(count , even , fib , *args):
    # get parameters
    x , *numbers , last = args
    print("--Generator Playground--")

    ans = ""
    # count down
    # for handles itslef otherwise we have to call generator function in next() evrytime until 1 reaches
    for i in count(x):
        ans+= f"{i} ->"
    print(f"countdown from {x}:")
    print(ans[:-2])
    print()

    # get even numbers
    print(f"Even numbers from {numbers[0]}: ")
    ans = ""
    for i in even(numbers[0]):
        ans += f"{i} "
    print(ans)

    # get fibonacci numbers
    print()
    print(f"Fibonacci Numbers up to {y}")
    ans = ""
    for i in fib(y):
        ans+= f"{i},"
    print(ans[:-1])

while True:
    x = int(input("Enter number to start countdown: "))
    try:
        if x<0:
            raise ValueError("ValueError: number must be positive!")
        break
    except ValueError as e:
        print(e)
numbers = input("Enter numbers  for applying even filters : ").split()
numbers = [int(x) for x in numbers]


while True:
    y = int(input("Enter number to calculate fibonacci : "))
    try:
        if y<0:
            raise ValueError("ValueError: number must be positive!")
        break
    except ValueError as e:
        print(e)

helper(countdown ,even_filter , fibonacci_gen , x , numbers , y)