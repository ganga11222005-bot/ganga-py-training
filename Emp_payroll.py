from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name: str):
        self.name = name
    
    @abstractmethod
    def cal_salary(self):
        """calculate the salary in subclasses"""
        pass
        

class permanent_Employee(Employee):

    Fixed_salary = 50000

    def cal_salary(self) -> float:
        return self.Fixed_salary
    

class contract_Employee(Employee):

    hourly_rate = 500
    hours_worked = 80

    def cal_salary(self) -> float:
        return self.hourly_rate * self.hours_worked


# Main program
name = input("Enter name:")
employee_type = input("Employee Type: ").strip().lower()

if employee_type == "permanent":
    employee = permanent_Employee(name)
elif employee_type == "contract":
    employee = contract_Employee(name)
else:
    print("Invalid employee type")

print(f"Salary: {employee.cal_salary()}")