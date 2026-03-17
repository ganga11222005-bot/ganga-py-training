class Animal:
    def eat(self):
        print("Animal is eating")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

#object creation
d = Dog()
d.eat()
d.bark()
