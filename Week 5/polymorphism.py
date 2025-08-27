# Activity 2: Polymorphism Example

class Vehicle:
    def move(self):
        print("The vehicle moves")

class Car(Vehicle):
    def move(self):
        print("The car drives on the road ")

class Plane(Vehicle):
    def move(self):
        print("The plane flies in the sky ")

# create objects
v1 = Car()
v2 = Plane()

# test polymorphism
v1.move()   # The car drives on the road 
v2.move()   # The plane flies in the sky 
