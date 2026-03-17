from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, days: int):
        self.days = days

    @abstractmethod
    def cal_rent(self) -> float:
        pass


class Car(Vehicle):
    rent_per_day = 1000

    def cal_rent(self):
        return self.days * self.rent_per_day


class Bike(Vehicle):
    rent_per_day = 500

    def cal_rent(self):
        return self.days * self.rent_per_day

# main program
days = int(input("Enter the number of days:"))
vehicle_type = input("Enter vehicle type(Car/Bike):").strip().lower()

if vehicle_type == "car":
    vehicle = Car(days)
    print(f"Car: Rent is {vehicle.rent_per_day}")
elif vehicle_type == "bike":
    vehicle = Bike(days)
    print(f"Bike: Rent is {vehicle.rent_per_day}")
else:
    print("*******INVALID VEHICLE TYPE*******")
print("----------------------------------------")
print(f"Total rent: {vehicle.cal_rent()}")
print("----------------------------------------")