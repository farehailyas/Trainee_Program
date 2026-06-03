class wrongOperator(Exception):
    pass
def calculator():
    while(True):
        print("____________________________________________________________________")
        print("This calculator performs simple arithmetic operations(+ , - , * , /)");
        ans = 0
        while True:
            try:
                x = float(input("Enter first number "))
                break
            except (ValueError , TypeError) as e:
                print("Invalid input. Please enter valid numbers") 
        while True:
            try:
                y = float(input("Enter second number "))
                break
            except (ValueError , TypeError) as e:
                print("Invalid input. Please enter valid numbers") 
        while True:
            try: 
                op = input("Enter operator ")
                
                if(op == "+"):
                    ans = x + y
                elif(op == "-"):
                    ans = x - y
                elif(op == "*"):
                    ans = x * y
                elif(op == "/"):
                    if y == 0:
                        raise ZeroDivisionError("Cannot divide by zero. Please enter a valid number")
                    else:   
                        ans = x // y   
                else:
                    raise wrongOperator("Invalid Operation. Please enter a valid operation(+ , - , * , /)")
                break  
            except wrongOperator as e:
                print(e)  
            except ZeroDivisionError as e:
                print(e) 
                break
        
        print("Result " , ans)
        print("Enter 1 to continue or -1 to exit")
        choice = int(input())
        if choice == -1:
            break     
            
calculator()