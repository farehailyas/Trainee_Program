# custom exception class
class NegativeNumberError(Exception):
    def __init__(self , val , msg):
        self.val = val
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return f"Error: {self.msg} Got:{self.val}"

print("--Safe Division Tool")
while True:
    flag = False
    # input first number untill user enters correct one
    while True:
        try:
            x = input("Enter first number (or 'quit' to exit): ")
            if x == "quit":
                print("Goodbye!")
                flag = True
                break
            x =  int(x)
            if x < 0:
                raise NegativeNumberError(x,"Negative numbers are not allowed!") 
            break
        except ValueError as e:
            print(f"Error: Please enter valid numbers!") 
        except NegativeNumberError as e:
            print(e)   
    if flag:
        break
    # input second number untill user enters correct one
    while True:
        try:
            y = int(input("Enter second number: "))
            if y == 0:
                raise ZeroDivisionError("Error: Cannot divide by zero!")
            elif y < 0:
                raise NegativeNumberError(y,"Negative numbers are not allowed!")
            else:
                break
        except ValueError:
            print(f"Error: Please enter valid numbers!")  
        except ZeroDivisionError as e:
            print(e)
        except NegativeNumberError as e:
            print(e)
   
    print(f"Result: {x/y}")
    print("Operation completed successfully")
    print()