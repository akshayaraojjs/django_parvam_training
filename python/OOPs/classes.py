# OOPs - Object Oriented Programming
# Class, Object, Abstraction, Encapsulation & Polymorphism
# Constructors, Access Modifiers, ...

# Class - Blueprint
# Object - Instance/Copy of Class

# Syntax: class className:
                # data members 
                # member functions()
                
# class Student{
    # int id, string name;
    # void showStudent(){
        # cout << "This shows the student details" 
    # }
    # void setName(string name){
    #    name = name; 
    # }
# };
# Student Stu1; - Object Created for Student
# Example: 1
class Student:
    # member function(self):  # self is a default parameter which expects the object to be passed as the argument
    # Assume "self" keyword as the "Object"
    def showStudent(self):
        print("This is a Student Class to show the student details")
        
    def showName(self, stuName):
        # In general, we can assume that data members can be called as Attributes & member functions are called as Behavior
        self.name = stuName   # datamember = value passed during the function call is assigned
        # self.name is the data member, stuName is the argument passed while calling the member function
        # It acts like a Setter Function
        print("Name of the Student: ", self.name)
        
    def setDetails(self, stuBranch, stuSection, stuSem):
        self.branch = stuBranch
        self.section = stuSection
        self.sem = stuSem
        # Data Members: branch, section & sem
        # print("Branch: ", self.branch, " Section:", self.section, " Sem:", self.sem)
        print(f" Branch:{self.branch}, Section: {self.section}, Sem: {self.sem}")
    
Stu1 = Student() # Object Stu1 has been created for the Student Class
# Syntax:
# object_name = classname()
Stu2 = Student() # Object 2

# Method 1 for calling the member function
# Syntax: ClassName.member_function(object)
Student.showStudent(Stu1)  # Calling the Member Function from Object Stu1
# self parameter in the member function accepts the object Stu1 as the argument
# Method 2:
Stu2.showStudent()
# self parameter automatically accepts the object Stu2 while calling the member function

Stu1.showName("Akshay")

Stu2.showName("Ajay")

Stu1.setDetails("ECE", "A", 8)

Stu2.setDetails("CSE", "C", 6)

# Example 2:
class Car:
    # Constructor (__init__)
    # Constructor is called Automatically when object gets created
    # __function_name__ - Special Functions
    def __init__(self):
        self.brand = "Toyota"
        self.price = 10.5
        self.fuel = "EV"
        print("Constructor has been called!")
    
    def showCarDetails(self):
        print(f"Car Brand: {self.brand}, Fuel: {self.fuel}, Price: {self.price}")

c1 = Car() # Object created for Car Class
c2 = Car() # Constructor is called here automatically

c1.showCarDetails()

c2.brand = "Tata"
c2.fuel = "Petrol"
c2.showCarDetails()


