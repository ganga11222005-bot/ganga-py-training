from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount: float):
        self.amount = amount

    @abstractmethod
    def pay(self):
        """Process the payment"""
        pass 


class UPI(Payment):
    """Payment using UPI"""
    def pay(self):
        print(f"Paid ₹ {self.amount} using UPI")


class Card(Payment):
    """Payment using Card"""
    def pay(self):
        print(f"Paid ₹ {self.amount} using Card")


class Cash(Payment):
    """Payment using Cash"""
    def pay(self):
        print(f"Paid ₹ {self.amount} using Cash")

# main program
Payment_mode = input("Enter the payment mode(UPI/Card/Cash):").strip().lower()
amount = float(input("Enter the amount:"))

if Payment_mode == "upi":
    payment = UPI(amount)
elif Payment_mode == "card":
    payment = Card(amount)
elif Payment_mode == "cash":
    payment = Cash(amount)
else:
    print("*****INVALID PAYMENT MODE*****")

payment.pay()