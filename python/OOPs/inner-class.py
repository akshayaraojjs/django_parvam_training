# inner class - Class within another Class
# Mobile Class - Outer Class
# Sim Class - Inner Class of Mobile Class/Outer Class
class Mobile:
    def __init__(self):
        self.brand = ""
        self.price = ""
        self.variant = ""
        # Type 1 - Inner Class Object
        self.sim = self.Sim() # Comment this while using Type 2 method
        
    def addDetails(self, Mbrand, MPrice, MVariant):
        self.brand = Mbrand
        self.price = MPrice
        self.variant = MVariant
    
    def showMobile(self):
        print(f"I'm using {self.brand} smartphone which has costed me Rs.{self.price} and it consists of {self.variant}")
        # Comment this while using Type 2 method
        self.sim.showSim() # calling the Instance Method of inner class from outer class
    
    # Inner Class within the Outer Class
    class Sim:
        def __init__(self):
            self.type = ""
            self.provider = ""
        
        def addDetails(self, simType, simProvider):
            self.type = simType
            self.provider = simProvider
            
        def showSim(self):
            print(f"I'm using {self.provider} sim with {self.type} plan")

phone1 = Mobile()

phone1.addDetails("Samsung - S22 Ultra", 50000, "12gb & 256gb")
phone1.sim.addDetails("5g", "Jio")  # calling setter of Inner Class 
phone1.showMobile()

# Object of Inner Class - Making a seperate Object
# sim1 = Mobile.Sim()

# sim1.addDetails("5g", "Jio")
# sim1.showSim()

# We can assign the value to the Inner Class's(Sim) - Instance Variable(type) by directly accessing the sim object which was defined in the Mobile Class constructor

# phone1.sim.type = "5g"

# print(phone1.sim.type)
# sim = Mobile.Sim() #Type 2 - Object for Inner Class
# Syntax:
# obj = OuterClassName.InnerClassName()
# sim.type = "5g"
# sim.provider = "Jio"

