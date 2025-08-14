class Result:
    def __init__(self):
        self.name = ""
        self.sub1 = ""
        self.sub2 = ""
        self.sub3 = ""
        
    def addMarks(self, sName, m1, m2, m3):
        self.name = sName
        self.sub1 = m1
        self.sub2 = m2
        self.sub3 = m3
        
    def showMarks(self):
        print("Marks for the respective subjects")
        print(f"Sub1: {self.sub1}, Sub2: {self.sub2}, Sub3: {self.sub3}")
        
    def __add__(self, other):    
        return self.sub1 + self.sub2 + self.sub3
    
    def __gt__(self, other):    
        total1 = self.sub1 + self.sub2 + self.sub3
        total2 = other.sub1 + other.sub2 + other.sub3
        if total1 > total2:
            return True
        else:
            return False
        
    def __repr__(self):
        return f"name={self.name}, sub1={self.sub1}, sub2={self.sub2}, sub3={self.sub3}"
    
    def __str__(self):
        return f"{self.name}, Marks Scored: {self.__add__(self)}"
    
        
stu1 = Result()
stu2 = Result()

stu1.addMarks("Akshay",40, 65, 45)
stu2.addMarks("Ajay",45, 58, 64)

stu1.showMarks()
stu2.showMarks()

TotalMarks = stu1.__add__(stu2) # stu1 + stu2
print("Total Marks of 2 students",TotalMarks)

print("Student 1 Object consists of: ",stu1)  # __repr__ => __str__
print("Student 2 Object consists of: ",stu2)

if stu1.__gt__(stu2): 
    print("Topper",stu1.name)
else:
    print("Topper",stu2.name)

# If we try to print the object, we are going to get the address of the object
# Ex: print(stu1) => <__main__.Result object at 0x000001fd36b33110>
# To get the details of the object, we use dunder: __str__
# Ex: print(stu1) => Akshay, Marks Scored: 150

# Note:__str__ dunder is used to show the info to the general audience
# __repr__ is used to show the info to the developers

# __str__ dunder is called while accessing the object, even if we have both the dunders defined using Operator Overloading