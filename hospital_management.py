from abc import ABC, abstractmethod


class Patient(ABC):

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_bill(self) -> float:
        """Calculate patient bill."""
        pass


class InPatient(Patient):
    """In-patient with fixed hospital charges."""

    fixed_bill = 20000

    def calculate_bill(self) -> float:
        return self.fixed_bill


# Main Program 
name = input("Enter patient name:") 
patient_type = input("Patient Type: ").strip().lower()

if patient_type == "inpatient":
    patient = InPatient(name)
else:
    print("*****Invalid patient type*****")
    
print("-------------------------------------")
print(f"Total Bill: {patient.calculate_bill()}")
print("-------------------------------------")