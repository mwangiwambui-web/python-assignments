# Base class
class Vehicle:
    def move(self):
        print("The vehicle moves...")


# Subclass 1
class Car(Vehicle):
    def move(self):
        print("Driving on the road ")


# Subclass 2
class Plane(Vehicle):
    def move(self):
        print("Flying in the sky ")


# Subclass 3
class Boat(Vehicle):
    def move(self):
        print("Sailing on water ")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
