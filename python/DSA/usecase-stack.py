# Checking Balanced Paranthesis:
# ([a + b]*[c + d])
class checkParanthesis:
    def __init__(self):
        # stack is a class variable, we can give any name
        self.stack = [] # empty list
        
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            # pop() is a list method not a class method
            return self.stack.pop()
        return None
    
    def peek(self):
        # return self.stack[-1] if not self.is_empty() else None
        if not self.is_empty():
            return self.stack[-1]
        else:
            None
            
    def is_empty(self):
        return len(self.stack) == 0
    
def check_balance(expression):
    exp = checkParanthesis() #exp is an object to check the expression 
    for char in expression:
        if char in "({[":
            exp.push(char)
        elif char in ")}]":
            if exp.is_empty():
                return False
            top = exp.pop()
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                return False
    return exp.is_empty()

print(check_balance("(a + b)*(c + d)"))
print(check_balance("[a + b)*(c + d]"))

# (a + b)*(c + d)
# math_exp = "(a + b)*(c + d)"
# print(math_exp)

# math_list = []
# for sym in math_exp:
#     # print(sym)
#     if sym in "({[":
#         print("True")
#         math_list.append(sym)
#     print(math_list)

# [(a+b)*(c+d)]
# [ ( a + b ) * ( c + d ) ] => 13 symbols in expression
            # stack = []
#Step1: if "[" in "[({" => T
            # stack = [ "[" ]
            # is_empty() => F
#Step2: if "(" in "[({" => T
            # stack = [ "[", "(" ]
            # is_empty() => F
#Step3: if "a" in "[({" => F
#           elif "a" in "])}" => F
#Step4: if "+" in "[({" => F
#           elif "+" in "])}" => F
#Step5: if "b" in "[({" => F
#           elif "b" in "])}" => F

# stack = [ "[", "(" ]
#Step6: if ")" in "[({" => F
#           elif ")" in "])}" => T
            # if stack.is_empty() = F
            # top = stack.pop() => top =  ["("]
            # stack = [ "[" ]
            # if top == "(" and sym != ')': => T & F => F
            # True
#Step7: if "*" in "[({" => F
#           elif "*" in "])}" => F
#Step8: if "(" in "[({" => T
            # second opening bracket added to the list   
            # stack = ["[", "("]
            # is_empty() => F
#Step9: if "c" in "[({" => F
#           elif "c" in "])}" => F
#Step10: if "+" in "[({" => F
#           elif "+" in "])}" => F
#Step11: if "d" in "[({" => F
#           elif "d" in "])}" => F
#Step12: if ")" in "[({" => F
        #   elif ")"f in "])}" => T
            # if stack.is_empty() => F
            # stack = ["[", "("] # Before pop
            # top = stack.pop() => top = ["("] 
            # stack = ["["] # After pop
            # if top == "(" and sym != ")" => True & False : False
            # Return True
# Step13: if "]" in "[({" => F
            # elif "]" in "])}" => T
            # if stack.is_empty() => F
            # stack = ["["] # Before pop
            # top = stack.pop() => top = ["["] 
            # stack = [] # After pop
            # if top == "[" and sym != "]" => True & False : False
            # Return True
        # stack.is_empty() => True
    # True => Expression is written correctly
    
# Tracing 2:
# [a+b)
# [, a, +, b, ) => 5 items
# step1: if "[" in "[({" => T
            # stack = ["["]
            # stack.is_empty() => F
# step2: if "a" in "[({" => F
            # elif "a" in "])}" => F
# step3: if "+" in "[({" => F
            # elif "+" in "])}" => F
# step4: if "b" in "[({" => F
            # elif "b" in "])}" => F
# step5: if ")" in "[({" => F
            # elif ")" in "])}" => T
            # if stack.is_empty() => F
            # stack = ["["] # Before pop
            # top = stack.pop() => top = ["["]
            # stack = [] # After pop
            # if top == "[" and char != "]" => True & True => True
            # Return False
        # False => Expression is not written correctly