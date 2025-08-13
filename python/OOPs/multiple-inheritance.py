# Multiple Inheritance: Multiple Base Class derives a Sub-Class
# Person & Student -> Developer
class Person:
    def __init__(self):
        self.name = ""
        self.age = ""
        
    def register(self, Name, Age):
        self.name = Name
        self.age = Age
        
    def details(self):
        print(f"My name is {self.name}, and I'm {self.age} years old")
        
class Student:
    def __init__(self):
        self.collage = ""
        self.branch = ""
        
    def enroll(self, stuCollege, stuBranch):
        self.collage = stuCollege
        self.branch = stuBranch
        
    def studentDetails(self):
        print(f"I'm currently studying in {self.collage} at {self.branch} branch.")
        
# Sub-Class with 2 Base Class
# Syntax: class SubClass(Class1, Class2)
class Developer(Student,Person):
    def __init__(self):
        self.company = ""
        self.role = ""
        
    def join(self, devCompany, devRole):
        self.company = devCompany
        self.role = devRole
        
    def devDetails(self):
        print(f"I'm currently working at {self.company} as a {self.role}.")
        
person1 = Person() # Object of Person Class (can access only its variables & methods)
person1.register("Akshay Rao", 24)
person1.details()
print("-------------------------")

student1 = Student() # Object of Student Class (can access only its variables & methods)
student1.enroll("GECK", "ECE")
student1.studentDetails()
print("-------------------------")

developer1 = Developer() # Object of Student Class (can access Person as well as Student)
developer1.register("Akshay Rao", 24)
developer1.details()
developer1.enroll("GECK", "ECE")
developer1.studentDetails()
developer1.join("ParvaM", "Technical Trainer")
developer1.devDetails()
print("-------------------------")