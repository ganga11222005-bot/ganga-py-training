from abc import ABC, abstractmethod

class Bank_Account(ABC):
    def __init__(self,name: str, balance: float):
        self.name = name
        self._balance = balance   # Encapsulation is applied
    

    def get_balance(self) -> float:
        return self._balance
    

    @abstractmethod
    def cal_interest(self) -> float:
        """Calculate interest in subclasses)."""
        pass


class Saving_Account(Bank_Account):
     # Applying 4% of interest
     interest_rate = 0.04
     def cal_interest(self) -> float:
         return self._balance * self.interest_rate
     
# Main program
print("**********Enter your details**********")
name = input("Enter your Name:")
balance = float(input("Enter your bank Balance:"))

account = Saving_Account(name, balance) 
print(" ")
print(f"Your bank Balance: {account.get_balance()}")
print(f"Calculated Interest: {account.cal_interest()}")