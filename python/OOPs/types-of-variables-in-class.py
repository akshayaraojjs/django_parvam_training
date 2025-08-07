# We have 2 types of Variables:
# 1) Instance Variables (Variables declared within the method)
# 2) Class Variables / Static Variables (Variables declared outside the method and within the class)
class College:
    accrediation = "AICTE" # class variable
    state = "Karnataka" # class variable
    # Constructor
    def __init__(self):
        # name, address, affliation, branches - instance variables (Working with Objects - so we need to use "self" keyword)
        self.name = "GEC Kushalnagar"
        self.address = "Kushalnagar"
        self.affliation = "VTU"
        self.branches = 4
        
    # Method
    def showCollege(self):
        print(f"Studied in {self.name}, located at {self.address} which is affliated to {self.affliation} university and offers the curriculum in {self.branches} different branches.")
        
    # We are working with class variable, so we need to use the "cls" as the paramter within the method and to access the class variable we need to refer to Class directly
    # Ex: def method(cls):
    # class_name.class_variable
    def showAccrediation(cls):
        print(f"College is accrediated with respect to {College.accrediation} and all colleges are located at {College.state}")
        # Here in the above example: "College" class is referring to "accrediation" class variable
College.accrediation = "NAAC"

col1 = College() # Object has been created

col1.showCollege()

col1.showAccrediation()

col2 = College() # Object has been created
col2.name = "GEC Koppal"

col2.showCollege()

col2.showAccrediation()

col3 = College()

col3.showAccrediation()

col3.name = "GEC Hassan"
col3.showCollege()

# Example 2: 
class Employee:
    # Namespace refers to the storage
    # class/static variables are stored in "Class Namespace"
    company = "ParvaM" 
    location = "Chikkabanavara"
     
    def __init__(self, e_name, e_age, e_role):
        # Instance Variables are stored in "Instance Namespace"
        self.name = e_name
        self.age = e_age
        self.role = e_role
        
    def showEmployee(self):
        print(f"My name is {self.name}, I'm {self.age} years old and I'm working as a {self.role} in my company.")
        
    def showCompanyDetails(cls):
        print(f"I'm working in {Employee.company}, which is located at {Employee.location}")

# Taking user input & assigning it to the 3 variables: emp_name, emp_age & emp_role
emp_name = input("Enter your name: ")

emp_age = int(input("Enter your age: "))

emp_role = input("Enter your role: ")

emp1 = Employee(emp_name, emp_age, emp_role)
# While creating object, we're passing the values to the Constructor

emp1.showEmployee()

emp1.showCompanyDetails() 

emp2 = Employee("Murthy", 23, "Java Trainer")

emp2.showEmployee()

emp2.showCompanyDetails()