# custom exception class
class UsernameTooShortError(Exception):
    def __init__(self , val , msg):
        self.val = val
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return f"Error: {self.msg} Got:{self.val}"

class WeakPasswordError (Exception):
    def __init__(self , val , msg):
        self.val = val
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return f"Error: {self.msg} Got:{self.val}"


def safe_divide(a , b):
    try:
        x = int(a)
        y = int(b)

        if y == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero!")
        print(x/y)
    except ValueError:
        print(f"Error:Second number is Invalid!")  
    except ZeroDivisionError as e:
        print(e)

    finally:
        print("Operation complete!")
       
safe_divide(10 , 2)
safe_divide( 5, 0 )
safe_divide("x" , 3)

def register(user , password):
    try:

        if len(user) < 4:
            raise UsernameTooShortError(user , "Username is too short")
        if len(password) < 8 :
            raise WeakPasswordError(password , "Passwords is week. length should be >= 8")
        
        flag = False
        for i in password:
            if i.isdigit():
                flag = True
                break
        if flag == False:
            raise WeakPasswordError(password , "Passwords is week . It must have some digit")
    except UsernameTooShortError as e:
        print(e)
    except WeakPasswordError as e:
        print(e) 

register("farehaa" , "gyhtyusiu")