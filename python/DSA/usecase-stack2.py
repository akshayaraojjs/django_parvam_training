# TextEditor Mock

# Write -> Undo -> Redo

class TextEditor:
    def __init__(self):
        # empty string to store some text
        self.text = "" # To add some text
        self.undo_stack = [] # empty list to store the undo items
        self.redo_stack = [] # empty list to store the redo items
    
    # Acting as push
    def write(self, add_word):
        # newly written
        self.undo_stack.append(self.text)
        # self.text = self.text + add_word # To update the existing text
        self.text += add_word # To update the existing text
        
    # Acting as pop
    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text) # keeping the backup of full sentence in redo_stack
            # print("Backup:",self.redo_stack)
            # updating the text after pop, removed the last sentence
            self.text = self.undo_stack.pop()
            # print("After Undo:", self.text)
        else:
            print("Undo cannot be done")
            
    def redo(self):
        if self.redo_stack:
            # updating the text in undo_stack
            self.undo_stack.append(self.text)
            # After updating the text, removing the history
            # print("Before Redo: ", self.redo_stack)
            self.text = self.redo_stack.pop()
            # print("After Redo: ", self.redo_stack)
        else:
            print("Redo cannot be done")
            
        
    def show(self):
        print("You're sentence contains: ", self.text)
        
vs_code = TextEditor()
vs_code.write("We are working on Python DSA.")
vs_code.write("Completed the Stack and its usecase.")
vs_code.write("Adding the 3rd sentence.")
vs_code.show()
vs_code.undo()
vs_code.show()
vs_code.redo()
# Tracing:
# sentence1 = "My name is akshay"
# sentence2 = "I'm 24 years old"
# sentence3 = "I'm currently handling Python DSA"
# stack = []

# stack.append(sentence1)
# stack.append(sentence2)
# stack.append(sentence3)
# print(stack)
# stack.pop()
# stack.pop()
# stack.append(sentence3)
# print(stack)


