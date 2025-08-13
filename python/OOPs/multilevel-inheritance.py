# Multi-Level Inheritance: Sub-Class deriving another Sub-Class
# Person -> Student -> Developer
# Base Class 
class Person:
    def __init__(self):
        self.name = ""
        self.age = ""
        
    def register(self, Name, Age):
        self.name = Name
        self.age = Age
        
    def details(self):
        print(f"My name is {self.name}, and I'm {self.age} years old")
        
# Sub-Class of (Person) Base Class
class Student(Person):
    def __init__(self):
        self.collage = ""
        self.branch = ""
        
    def enroll(self, stuCollege, stuBranch):
        self.collage = stuCollege
        self.branch = stuBranch
        
    def studentDetails(self):
        print(f"I'm currently studying in {self.collage} at {self.branch} branch.")
        
# Sub-Class of Student(Base Class or Sub-Class of (Person) Base Class)
class Developer(Student):
    def __init__(self):
        self.company = ""
        self.role = ""
        
    def join(self, devCompany, devRole):
        self.company = devCompany
        self.role = devRole
        
    def devDetails(self):
        print(f"I'm currently working at {self.company} as a {self.role}.")
        
student1 = Student() # Object of Student Class (can access Person)
student1.register("Akshay Rao", 24)
student1.details()
student1.enroll("GECK", "ECE")
student1.studentDetails()

developer1 = Developer() # Object of Student Class (can access Person as well as Student)
developer1.register("Akshay Rao", 24)
developer1.details()
developer1.enroll("GECK", "ECE")
developer1.studentDetails()
developer1.join("ParvaM", "Technical Trainer")
developer1.devDetails()