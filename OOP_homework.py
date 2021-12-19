#Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.
class Rectangle:
    def __init__(self,lenght,width):
        self.lenght=lenght
        self.width=width
    def computeArea(self):
        return self.width*self.lenght

r=Rectangle(2,5) 
print(r.computeArea())
#Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

#Create a Vehicle class without any variables and methods.
class Vehicle2:
    def __init__(self) -> None:
        pass

#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    def __init__(self,max_speed,mileage):
        super().__init__(max_speed,mileage)

b=Bus(max_speed=500,mileage=100)
print("Bus max speed :", b.max_speed)
print("Bus mileage :", b.mileage)