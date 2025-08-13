class Laptop:
    
    # Class/ Static Variable
    operatingSystem = "Windows"
    
    def __init__(self):
        # 5 instance variables
        self.brand = "N/A"
        self.model = "N/A"
        self.processor = "N/A"
        self.ram = "N/A"
        self.storage = "N/A"
       
    # Mutator Method - Instance Method 
    def buyLaptop(self, lapBrand, lapModel, lapProcessor, lapRAM, lapStorage):
        self.brand = lapBrand
        self.model = lapModel
        self.processor = lapProcessor
        self.ram = lapRAM
        self.storage = lapStorage
        
    # Accessor Method - Instance Method
    def useLaptop(self):
        print(f"I'm using {self.brand} laptop - {self.model} model, which consists of {self.processor} proccessor with {self.ram}gb RAM and {self.storage}gb of Storage.")
        
    @classmethod
    def showOS(cls):
        print(f"My Laptop works with {cls.operatingSystem} OS.")
        
    @staticmethod
    def place():
        print("I bought my laptop from the Showroom")
        
lap1 = Laptop()
lap2 = Laptop()

lBrand = input("Enter the brand:")
lModel = input("Enter the model:")
lProcessor = input("Enter the processor:")
lRam = input("Enter the ram:")
lStorage = input("Enter the storage:")

Laptop.showOS()

Laptop.place()

lap1.buyLaptop(lBrand, lModel, lProcessor, lRam, lStorage)

lap2.buyLaptop("HP", "Victus", "Intel i5 10th gen", 8, 512)

lap1.useLaptop()
lap2.useLaptop()