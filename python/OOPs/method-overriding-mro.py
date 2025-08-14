# method overriding: same methods present in different classes
# Multiple Inheritance: Animal & Dog -> Puppy
class Animal:
    def __init__(self):
        self.type = ""
        print("Animal Constructor has been called!")
        
    def add(self, Type):
        self.type = Type
        
    def show(self):
        print(f"This is a {self.type} animal")
        
class Dog:
    def __init__(self):
        self.name = ""
        print("Dog Constructor has been called!")
        
    def add(self, Name, AType):
        self.dname = Name
        
    def show(self):
        print(f"Name of the Dog: {self.dname}")

# MRO - Method Resolution Order
# Priority for the overriding applies from left to right
class Puppy(Animal, Dog):
    def __init__(self):
        self.pname = ""
        # Calling the constructor of Base Class
        super().__init__()
        print("Puppy Constructor has been called!")
        
    def add(self, pName, AType):
        # Calling the add method defined in the Base Class (Animal)
        super().add(AType)
        self.pname = pName
        
    def show(self):
        # Calling the show method defined in the Base Class (Animal)
        super().show()
        print(f"Name of the puppy: {self.pname}")

puppy1 = Puppy() # dog object of Dog sub-class can access the variables & methods of Animal class
puppy1.add("Ramu", "Carnivore")
puppy1.show()