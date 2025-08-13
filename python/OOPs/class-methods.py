# We have 3 types of Methods:
# 1) Instance Method:
#   a) Accessor Method (getter)
#   b) Mutator Method (setter)
# 2) Class Method
# 3) Static Method


# self parameter expects the Oject (Instance Method)
# cls parameter expects the Class (Class Method)
# no parameter is required for Static Method

class KSRTC:
    # Class Variables
    govt = "GoK"
    dept = "Transport Dept"
    
    # constructor to assign the default values
    def __init__(self):
        self.division = "N/A"
        self.depot = []
        self.route = "N/A"
        
    # instance method
    # Mutator Method assigning the values for the Instance Variables (Setter)
    def setRoute(self, Bdivisions, Bdepot, Broute):
        self.division = Bdivisions
        self.depot = Bdepot
        self.route = Broute
        
    # Accessor Method is fetching the details from the Instance Variables (Getter)
    def getRoute(self):
        print(f"Bus comes under {self.division}, which consits of the following depot: {self.depot}. And bus will travel through {self.route}")
        
    # To access class variable, we use "cls" parameter
    # Decorator - "@classmethod" is used to define the class methods to work on class variables
    @classmethod
    def showDetails(cls):
        # To access the class variables, we should refer to Class, Ex: className.class_variable / cls.class_variable
        print(f"Managed by {KSRTC.govt}, under {cls.dept}.")
       
    # Decorator - "@staticmethod" is used to work with static method, which not related to class or object 
    # For Static Method, parameter is left empty, or not used
    @staticmethod
    def showInfo():
        print("We are travelling via Bus")
        
bus1 = KSRTC()  # Defined the Object of KSRTC class

bus2 = KSRTC()

busDivision = input("Enter the Bus Division:")

busDepotRaw = input("Enter the Bus Depot Details seperated by a space:")
print(type(busDepotRaw))

busDepot = list(busDepotRaw.split())
busRoute = input("Enter the Bus Route:")

bus1.setRoute(busDivision, busDepot, busRoute)

bus1.getRoute()
bus2.getRoute()

# Calling the Class Method from Class
KSRTC.showDetails()

# Calling the Static Method from Class
KSRTC.showInfo()