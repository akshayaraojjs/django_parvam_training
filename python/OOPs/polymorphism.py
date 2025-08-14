# Polymorphism means Same Name with Multiple forms
# 4 types:
# 1) Duck Typing
# 2) Operator Overloading
# 3) Method Overloading
# 4) Method Overriding

# 1) Duck Typing (Dynamic Typing)
# Different Objects acting with a same behavior

class Car:
    def start(self):
        print("Car has been started")
        
    def drive(self):
        print("Car starting moving")
        
    def stop(self):
        print("Car has been stopped")
        
class Bus:
    def start(self):
        print("Bus has been started")
        
    def drive(self):
        print("Bus starting moving")
        
    def stop(self):
        print("Bus has been stopped")
    
# function or method not associated with any of the class
# We can use any parameter, not only object, we can use obj, self, or anything else but it expects a Object while calling this method
def showInfo(object):
    object.start()
    object.drive()
    object.stop()
    
car1 = Car() # Object has been created for Car Class
bus1 = Bus() # Object has been created for Bus Class
showInfo(car1)
showInfo(bus1)

car1.start()

n = 5
print(n, type(n))
n = 25.5
print(n, type(n))
n = "Akshay"
print(n, type(n))

num1 = 3 # num1 = int()
num2 = 4
# print(num1 + num2)
print(num1.__add__(num2))
print(type(num1 + num2))

f1 = 20.5 # f1 = float()
f2 = 30.7
print(f1 + f2)
print(f1 > f2)
print(f1.__add__(f2))
print(type(f1 + f2))

s1 = "Akshay" # s1 = str()
s2 = "Rao"
print(s1 + s2)
print(s1.__add__(s2))
print(type(s1 + s2))

# In Python, all the datatypes are considered as the Class, the variables can be considered as Object

# Magic Methods(dunder): The inbuilt methods created for the datatypes(class) are called Magic Methods
# dunder: double underscore
# constructor : "__init__"
# + : "__add__"
# - : "__sub__"
# * : "__mul__"
# > : "__gt__"
# < : "__lt__"
# <= : "__le__"
# >= : "__ge__"
# == : "__eq__"
# != : "__ne__"