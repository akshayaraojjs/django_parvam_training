# Using Python List we can create a stack
class Stack:
    # Constructor
    def __init__(self):
        self.stack = [] # Empty List called stack
        
    def push(self, item):
        # Append method is used to add the data in the list(now it is stack)
        self.stack.append(item)
        print(f"New Item has been pushed: {item}") # message to confirm that the item has been added
        print("Stack after push:", self.stack)
        
    def pop(self):
        # if (not 0) => 1
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack Underflow! Item cannot be popped out"
        
    # Show Last Item from the stack (Top)
    def peek(self):
        if not self.is_empty():
            # -1 is reffering to Negative Indexing
            return self.stack[-1]
        else:
            return "Stack is empty!"
        
    def is_empty(self):
        # Comparing whether the stack size is 0, Returns the False(0)
        return len(self.stack) == 0
    
    def size(self):
        # len method is used to check the size of the list(now it is stack)
        return len(self.stack)
    
# Creating a Stack Object
stack1 = Stack() # stack1 is a object of Stack class
stack1.push(5)
stack1.push(10)
stack1.push(15)
stack1.push(20)
stack1.push(25)
print("Stack Size:", stack1.size())

print("Top Element:", stack1.peek())
print("Popping an item:", stack1.pop())
print("Stack Size:", stack1.size())
print("Popping an item:", stack1.pop())
print("Popping an item:", stack1.pop())
print("Popping an item:", stack1.pop())
print("Stack contains:", stack1.stack)
print("Stack Size:", stack1.size())
print("Is Stack Empty?", stack1.is_empty())