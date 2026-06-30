from abc import ABC , abstractmethod
class Patient:
    def __init__(self, name, age, ailment , recordNo=None , perscription = None):
        self.name = name
        self.age = age
        self.__ailment = ailment
        self.__recordNo = recordNo
        self.__perscription = perscription
    def get_summary(self):
        return f"Patient Name: {self.name}, Age: {self.age}, Ailment: {self.__ailment}"
    pass
    def __privateFunction(self):
        print("I am a private function")
   

class Staff(ABC):
    @abstractmethod
    def get_role(self):
        pass
    def check_in(self, patient):
        print(f"{self.get_role()} is checking in patient {patient.name}")

class Doctor(Staff):
    def __init__(self, name, specialization):
        self.name = name
        self.specialization = specialization
    def get_role(self):
        return "Doctor"
    def diagnose(self, patient):
        print(f"Doctor {self.name} is diagnosing patient {patient.name} with ailment {patient._Patient__ailment}")
    pass

class Nurse(Staff):
    def __init__(self, name):
        self.name = name
    def get_role(self):
        return "Nurse"
    def assist(self, doctor, patient):
        print(f"Nurse {self.name} is assisting Doctor {doctor.name} with patient {patient.name}")
    pass

# Example usage
patient1 = Patient("Ahmad", 30, "Flu" , perscription = "take rest")
# perscription = patient1.getPersecription()
# print(perscription)
print(patient1._Patient__perscription)
patient1._Patient__privateFunction()
patient2 = Patient("amna", 25, "Cold")
staff = []
staff.append(Doctor("Ali", "Physician"))
staff.append(Nurse("Sarah"))

for i in staff:
    i.check_in(patient1)
    i.check_in(patient2)
    if isinstance(i, Doctor):
        i.diagnose(patient1)
        i.diagnose(patient2)
    elif isinstance(i, Nurse):
        i.assist(staff[0], patient1)
        i.assist(staff[0], patient2)
    pass