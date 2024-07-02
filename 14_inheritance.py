# Inheritance 

class Vehicle:
    def general_usage(self):
        print("It is used for transportation")

class Car(Vehicle):
    def __init__(self, car):
        self.name = car
        print(f"I am a {self.name}")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print(f"{self.name} is used for commuting and leisure with family")

    def has_properties(self):
        print(f"{self.name} has {self.wheels} wheels and roof: {self.has_roof}")

class Bike(Vehicle):
    def __init__(self, bike):
        self.name = bike
        print(f"I am a {self.name}")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        print(f"{self.name} is used for racing and road trip")

    def has_properties(self):
        print(f"{self.name} has {self.wheels} wheels and roof: {self.has_roof}")

c = Car('car')
c.specific_usage()
c.has_properties()

b = Bike('bike')
b.general_usage()
b.specific_usage()
b.has_properties()

b = Bike('bike')
# propertise of an object can be changed
b.wheels = 3
b.general_usage()
b.specific_usage()
b.has_properties()


# 
print(isinstance(c, Car))
print(issubclass(Car,Vehicle))