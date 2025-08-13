# Single Inheritance: One Parent & One Child
# Base Class
# Person -> Student
class Person:
    def __init__(self):
        self.name = ""
        self.age = ""
        
    def register(self, Name, Age):
        self.name = Name
        self.age = Age
        
    def details(self):
        print(f"My name is {self.name}, and I'm {self.age} years old")
        
# Sub-Class
# Syntax:
# class Sub-Class-Name(Base-Class)
class Student(Person):
    def __init__(self):
        self.collage = ""
        self.branch = ""
        
    def enroll(self, stuCollege, stuBranch):
        self.collage = stuCollege
        self.branch = stuBranch
        
    def studentDetails(self):
        print(f"I'm currently studying in {self.collage} at {self.branch} branch.")
        
student1 = Student() # Object of Sub-Class
# Sub-Class can access the Variables of the Base Class
# student1.name = "Sudeep"
# student1.age = 22
# student1.collage = "GECK"
# student1.branch = "ECE"

# Sub-Class can also access the methods of the Base Class
student1.register("Akshay Rao", 24) # Calling the Instance Method of Base Class from Sub-Class
student1.details() # print details of the person

# Calling its own method
student1.enroll("GEC Kushalnagar", "ECE")
student1.studentDetails()