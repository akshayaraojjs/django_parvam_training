# method overriding: same methods present in different classes
class Animal:
    def __init__(self):
        self.type = ""
        print("Animal Constructor has been called!")
        
    def add(self, Type):
        self.type = Type
        
    def show(self):
        print(f"This is a {self.type} animal")
        
class Dog(Animal):
    def __init__(self):
        self.name = ""
        # Calling the constructor of Base Class
        super().__init__()
        print("Dog Constructor has been called!")
        
    def add(self, Name, AType):
        # Calling the add method defined in the Base Class (Animal)
        super().add(AType)
        self.name = Name
        
    def show(self):
        # Calling the show method defined in the Base Class (Animal)
        super().show()
        print(f"Name of the Dog: {self.name}")

dog1 = Dog() # dog object of Dog sub-class can access the variables & methods of Animal class
dog1.add("Ramu", "Carnivore")
dog1.show()