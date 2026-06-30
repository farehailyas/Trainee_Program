class CustomBalanceCheck(Exception):
    def __init__(self , balance , msg):
        self.balance = balance
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return f"{self.balance} -> {self.msg}"
print("getting name of class")
print(CustomBalanceCheck.__name__)

def checkBalance(x:float):
    if x < 0 :
        raise CustomBalanceCheck(x,"Balance cannot be negative")
    else:
        print("Your current balance is " ,x)

try:
    checkBalance(-8)
except CustomBalanceCheck as e:
    print(e)
    # HERE E CALLS str obj to print info about object


# class CustomBalanceCheck():
#     def __init__(self , balance , msg):
#         self.balance = balance
#         self.msg = msg
#         # super().__init__(self.msg)
#     def __str__(self):
#         return f"{self.balance} -> {self.msg}"


# b = CustomBalanceCheck(6,"hello")
# print(b)