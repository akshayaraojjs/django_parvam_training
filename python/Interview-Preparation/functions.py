# Functions in Python
# Work on Repeatative Task
# 3 Parts of functions:
# 1) Function Declaration
# 2) Function Definition
# 3) Function Call
# def keyword is used to declare any function/method

# declared a function called "sayHello"
# def function_name():

# Basic Function
def sayHello(): # function declaration
    print("Say Hello function is called!") # function definition
    
sayHello() # function call

# Function with a parameter
def sayHi(name, age):
    # print("Hi ", name, ", you're ", age, " years old.")
    # f string
    print(f"Hi {name}, you're {age} years old.")
    
# While declaring a function, variables within the paranthesis is called as Parameters
# name & age are called as Parameters
    
# While calling the function, variables within the paranthesis is called as Arguments
# Akshay & 24 are called as Arguments
sayHi("Akshay", 24) 
sayHi("Chiranth", 22)
# sayHi("Manoj")

# We have 5 types of Arguments:
# 1) Positional Argument
# 2) Keyword Argument
# 3) Default Argument
# 4) Variable Length Arguments (*args, **kwargs)
# *args - Arbitrary Positional Argument
# **kwargs - Arbitrary Keyword Argument
# 5) Arbitrary Mix

# 1) Positional Argument
def showDetails(name, usn, branch, sem):
    print(f"Your name is {name} and you're bearing a USN: {usn}, and you're from {branch} branch, currently you're studying in {sem} sem")
    
showDetails("Akshay", "AR1234", "CSE", 8)
# Expecting 4 arguments, doesn't check the order of the argument
showDetails("CSE", 8, "Chiranth", "CR1234")

# 2) Keyword Argument
def showInfo(name, usn, branch, sem):
    print(f"Your name is {name} and you're bearing a USN: {usn}, and you're from {branch} branch, currently you're studying in {sem} sem")
    
# keyword is passed along with the arguments for more specificity
showInfo(name="Akshay", usn="AR1234", branch="CSE", sem=8)
showInfo(name="Chiranth", branch="ISE", sem=6, usn="CR1234")

# Positional Argument -> Default Argument
# 3) Default Argument
def showStudent(name, usn, sem, branch="CSE"):
    print(f"Your name is {name} and you're bearing a USN: {usn}, and you're from {branch} branch, currently you're studying in {sem} sem")

# No restriction while passing the arguments: It can a string, int, float
showStudent("Ajay", "AJ1234", 7)
showStudent("Akash", "AK1234", 7, "Civil")

# 4) Variable Length Arguments (*args, **kwargs)
# Argument count is not a priority, it will take any number of arguments
# args: Arbitrary Positional Arguments
# Used when the argument count is unknown
# add(1,4,3)
# add(1,4,3,6,7)
# add(1,4,3,6,7, 9, 10)

# To access each and every element from the tuple, we need to traverse it:
# Why Tuple: To avoid the duplication/forgery of value while calling the function
# Immutable, Ordered & can contain duplicate values
def add(*args):
    sum = 0
    print(args)
    print(type(args))
    for i in args:
        # print("Number:",i)
        sum = sum + i
        # print("Sum:",sum)
    print(f"Sum of given numbers: {sum}")
    
# Tuple is expected as the argument while using *args
add()
add(1, 5)
add(1, 5, 8, 10)
add(1, 5, 8, 10, 20, 30, 8, 5)

# kwargs: arbitrary keyword arguments 
# dictionary is accepted as the argument while using the kwargs
# key & value pairs are given
# why dict? We are expecting the keyword along with the value, so dictionary is more suitable for **kwargs
def bankDetails(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # items() method is used to fetch both key & value together
    # keys() method is used to fetch only keys
    # values() method is used to fetch only values
    for k, v in kwargs.items():
        print(f"{k} = {v}")
    print("----------")
        
# Keyword arguments should be passed while callin the kwargs function
bankDetails(name = "Akshay", acNo = 12345678, bank = "SBI", ifsc = "SBIN00123")
bankDetails(name = "Ajay", acNo = 12346678, bank = "Canara Bank")

# 5) Arbitrary Mix
# Positional argument, default arguments, args, kwargs
# Positional argument -> *args -> default args -> **kwargs
def mixture(name, *args, branch = "CSE", **kwargs):
    print(f"You're name is {name}, you're from {branch} branch")
    print(f"You're additional details are as follows:")
    for i in args:
        print(f"{i}")
        
    for key,value in kwargs.items():
        print(f"{key} : {value}")
    print("------------------")
mixture("Akshay", 24, college="RRIT", branch="ISE")
mixture("Ajay", 23, college="Dhanwantari", degree="MCA", sem = 3)
mixture("Manoj", college="GEC Kushalnagar", degree="B.Tech", status = "Passed Out", address = "Hassan")