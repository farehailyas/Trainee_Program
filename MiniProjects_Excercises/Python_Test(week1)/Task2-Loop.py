"""Part A : Star Triangle """

n = int(input("Enter any positive integer : "))

for i in range (n+1):
    for j in range (i):
        print("*" , end = " ")
    print()
    
"""Part B Fizz Buzz """

for i in range (50):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0: 
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(f"Number : {i}")

""" Part C pyramid """

n = 4
space = n
i = 1
while i<=4:
    j = 1 
    s = space
    while s > 0:
        print(end = " ")
        s-=1
        
    while j <= i:
        print(j , end="  ")
        j += 1
    print()    
    i+=1
    space-=1