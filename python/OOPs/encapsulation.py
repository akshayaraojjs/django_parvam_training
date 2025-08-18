# encapsulation - Binding Data
# Varaibles & Methods are binded together in a capsule format: Combining variables & methods
# We will access modifiers to bind variables & methods

# Access Modifiers:
# public - Can access everywhere in the class or outside the class
# Ex: name, showName()
# protected - Can access within the class and its sub-class
# Ex: _college, _showCollege()
# private - Can access only within class and we can access it via (name mangling method) outside the class (Not Recommended)
# Ex: __password, __showPassword()

class Bottle:
    def __init__(self):
        self.brand = "" # public variable
        self._modelNo = "" # protected variable
        self.__serialNo = "" # private variable
        
    def setDetails(self, brandName, modelNum, serialNum):
        self.brand = brandName
        self._modelNo = modelNum
        self.__serialNo = serialNum
        
        # protected method
    def _showModelNum(self):
        print(f"The Model Number of the bottle {self._modelNo}.")
        
        # private method
    def __showSerialNum(self):
        print(f"The Serial Number of the bottle {self.__serialNo}.")
        
        # public method
    def showDetails(self):
        print(f"This bottle is a product of {self.brand} brand.")
        # Calling Private & protected methods from public method internally
        # Standard method to call the private & protected methods
        self._showModelNum()
        self.__showSerialNum()
        
        # To call or access the private or protected method, we need to call it indirectly using public method
        
class Sipper(Bottle):
    def __init__(self):
        self.purpose = ""
        # Method Overriding
        super().__init__()
        
    def setPurpose(self, usage):
        self.purpose = usage
        
    def showAllDetails(self):
        print(f"This bottle can be used in {self.purpose}.")
        self._showModelNum()
        self.__showSerialNum()
        
bottle1 = Sipper() # object of Sipper - sub-class

bottle1.setDetails("Cello", "CEL1234", "CELLO123")

bottle1.showDetails()

print(bottle1._modelNo)
# If we try to access private data, we will be getting: AttributeError
# print(bottle1.__serialNo)
# Name Mangling Method:
# Syntax: object._BaseClass__privateVariable
print(bottle1._Bottle__serialNo)

# bottle1.__showSerialNum()
bottle1._Bottle__showSerialNum()

# Using name mangling method we can access the private data outside the class
# print(dir(bottle1)) # To check what all details we can access from this object - dir()