from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self , name , dept):
        self.name = name
        self.dept = dept

    @abstractmethod
    def calculate_pay(self):
        pass

    def display_info():
        print(f"{self.name} belongs to {self.dept}")

class FullTimeEmployee(Employee):
    def __init__(self , name , dept , sal):
        super().__init__(name , dept)
        self.__sal = sal
    def get_sal(self):
        return self.__sal

    def set_sal(self , sal):
        if sal<0:
            return "Salary cant be nagative"
        else:
            self.__sal = sal
    
    def calculate_pay(self):
        pay = self.__sal
        print(f"Calculating Bill in full time employee {pay}")
    
class ContractEmployee(Employee):
    def __init__(self , name , dept , hourly_rate , hours_worked):
        super().__init__(name , dept)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        pay = (self.hourly_rate * self.hours_worked)
        print(f"Calculating Bill in Contracted employee {pay}")

emp1 = FullTimeEmployee("Fareha" , "SE" , 1223456  )
emp2 = ContractEmployee("Ali" , "CS" , 10000 , 6)
lis = [emp1 , emp2]

for i in lis:
    i.calculate_pay()
    