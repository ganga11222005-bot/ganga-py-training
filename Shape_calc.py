from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self) -> float:
        """Calculate area of the shape."""
        pass


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, length: float, breadth: float):
        self.length = length
        self.breadth = breadth

    def area(self) -> float:
        return self.length * self.breadth


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius: float):
        self.pi = 3.14
        self.radius = radius

    def area(self) -> float:
        return self.pi * self.radius * self.radius


#  Main Program 

def main():
    print("1. Rectangle")
    print("2. Circle")

    choice = input("Choose shape (1/2): ").strip()

    if choice == "1":
        length = float(input("Enter length: "))
        breadth = float(input("Enter breadth: "))
        shape = Rectangle(length, breadth)
        print(f"Area of Rectangle: {shape.area()}")

    elif choice == "2":
        radius = float(input("Enter radius: "))
        shape = Circle(radius)
        print(f"Area of Circle: {shape.area():.2f}")

    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()