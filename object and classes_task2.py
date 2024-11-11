# 1.Define a class Rectangle with attributes
#  width and height.Add methods area and perimeter
#  to calculate the area and perimeter of the 
# rectangle.Instantiate a few rectangle objects 
# and print their area and perimeter.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
         return self.width * self.height
    def perimeter(self):
        return (self.width + self.height)*2
rectangle1 = Rectangle(9, 5)
rectangle2 = Rectangle(5, 3)
rectangle3 = Rectangle(7, 6)
print(f"Area of Rectangle 1 is: {rectangle1.area()}, Perimeter is: {rectangle1.perimeter()}")
print(f"Area of Rectangle 2 is: {rectangle2.area()}, Perimeter is:{rectangle2.perimeter()}")
print(f"Area of Rectangle 3 is: {rectangle3.area()}, Perimeter is: {rectangle3.perimeter()}")

# 2.Create a class Employee with attributes name
#  and salary.Add a method give_raise that increases
#  the salary by a given percentage.Instantiate an
#  employee, give them a raise, and display their 
# new salary.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def give_raise(self, percentage):
        self.salary= self.salary * (percentage / 100)
        return self.salary
employee1 = Employee ("Verah Michaels", 1000000)
employee1.give_raise(30)
print (f"Employee is: {employee1.name}, Salary of: {employee1.salary:}")    

# 3.Create a base class Vehicle with attributes 
# brand and model.
# Create two subclasses Car and Motorcycle that 
# inherit from Vehicle and add unique methods to
#  each subclass (e.g., honk for Car and rev_engine
#  for Motorcycle).
# Instantiate both subclasses and call their methods.
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model=model

class car(Vehicle):
    def honk(self):
        return f'{self.brand} {self.model} the car honks'
class motorcycle(Vehicle):
    def rev_engine(self):
        return f'{self.brand} {self.model} the motorcycle vrooms'
    

Vehicle1 =car("Toyota", "v8")
print(Vehicle1.honk())

Vehicle2 = motorcycle("Harley-Davidson", "Iron 883")
print(Vehicle2.rev_engine())




class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        return f'{self.name}makes sound'
    
class cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed=breed

    def sound(self):
        return super().sound()
cat1=cat('leon','leopard')
print(cat.name())



