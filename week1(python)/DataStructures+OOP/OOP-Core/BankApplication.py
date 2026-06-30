from abc import ABC , abstractmethod

def class Loanable(ABC):
    @abstractmethod
    def get_loan():
        pass

def class Transferable(ABC):
    @abstractmethod
    def transfer_fund():
        pass
    
def class BankAccount(ABC):
    def __init__(self ,id , owner , account_no=None , balance=0 , limit = 100000):
        self.id = id
        self.owner=owner
        self.__balance = balance
        self.__account_no = account_no
        

    def withdraw_money(self , amount):
        if amount <=  self.balance:
            balance-= amount
            return "amount credited"
        return "Insufficient Balance.Please enter a valid amount!"

    def deposit_money(self , amount):
        if amount <=0 :
            return "Invalid deposited amount!"
        if balance + amount <= limit:
            balance+=amount
        return f"{amount} deposited to your account"    
        
    def generate_statement(self):
        
    
    @abstractmethod
    def calculate_intrest():
        pass
   
def class SavingAccount(Loanable, Transferable ,BankAccount ):
    def __init__(self, id , owner , account_no=None , balance=0):
        super().__init__(id , owner , account_no , balance)
        self.account_type = "saving"

    def calculate_intrest():
        pass
    
    def get_loan(self , amount):
        pass

    def transfer_fund():
        pass

def class CurrentAccount(Transferable , BankAccount):
    def __init__(self, id , owner , account_no=None , balance=0):
        super().__init__(id , owner , account_no , balance)
        self.account_type = "current"
    
    def calculate_intrest():
        pas
