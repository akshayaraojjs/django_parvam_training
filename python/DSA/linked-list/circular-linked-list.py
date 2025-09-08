class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        if not self.head:
            print("List is Empty!")
            return
        current = self.head
        print("Circular Linked List: ", end = " ")
        while True:
            print(current.data, end = " -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")
        
    def insertStart(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            print(f"Inserted {value} as first node")
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        new_node.next = self.head
        last.next = new_node
        self.head = new_node
        print(f"Inserted {value} at Start")
        
    def insertEnd(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
            print(f"Inserted {value} as first node")
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        last.next = new_node
        new_node.next = self.head
        print(f"Inserted {value} at End")
        
    def insertAfterValue(self, target, value):
        if not self.head:
            print("List is Empty")
            return
        current = self.head
        while True:
            if current.data == target:
                new_node = Node(value)
                new_node.next = current.next
                current.next = new_node
                print(f"Inserted {value} after {target}")
                return
            current = current.next
            if current == self.head:
                break
        print(f"Node with value {target} not found")
        
    def insertBeforeValue(self, target, value):
        if not self.head:
            print("List is Empty")
            return
        current = self.head
        prev = None
        while True:
            if current.data == target:
                new_node = Node(value)
                if prev is None:
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    new_node.next = self.head
                    last.next = new_node
                    self.head = new_node
                else:
                    new_node.next = current
                    prev.next = new_node
                print(f"Inserted {value} before {target}")
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        print(f"Node with value {target} not found")
        
    def deleteStart(self):
        if not self.head:
            print("List is Empty")
            return
        if self.head.next == self.head:
            print(f"Deletd {self.head.data} (only node)")
            self.head = None
            return
        last = self.head
        while last.next != self.head:
            last = last.next
        print(f"Deleted {self.head.data} from start")
        last.next = self.head.next
        self.head = self.head.next
    
    def deleteEnd(self):
        if not self.head:
            print("List is Empty")
            return
        if self.head.next == self.head:
            print(f"Deletd {self.head.data} (only node)")
            self.head = None
            return
        prev = None
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
        print(f"Deleted {current.data} from end")
        prev.next = self.head
        
    def deleteValue(self, value):
        if not self.head:
            print("List is Empty")
            return
        current = self.head
        prev = None
        while True:
            if current.data == value:
                if prev is None:
                    if current.next == self.head:
                        self.head = None
                        print(f"Deleted {value} (only node)")
                        return
                    last = self.head
                    while last.next != self.head:
                        last = last.next
                    self.head = current.next
                    last.next = self.head
                else:
                    prev.next = current.next
                print(f"Deletd {value} from list")
                return
            prev = current
            current = current.next
            if current == self.head:
                break
        print(f"Node with value {value} not found")
    
cll = CircularLinkedList()

while True:
    print("\n Circular Linked List Menu:")
    print("1. Insert at Start")
    print("2. Insert at End")
    print("3. Insert After a Value")
    print("4. Insert Before a Value")
    print("5. Delete at Start")
    print("6. Delete at End")
    print("7. Delete by Value")
    print("8. Traverse the Linked List")
    print("9. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    
    if choice == 1:
        val = int(input("Enter a value:"))
        cll.insertStart(val)
    elif choice == 2:
        val = int(input("Enter a value:"))
        cll.insertEnd(val)
    elif choice == 3:
        target = int(input("Insert after which value?"))
        val = int(input("Enter a value:"))
        cll.insertAfterValue(target, val)
    elif choice == 4:
        target = int(input("Insert before which value?"))
        val = int(input("Enter a value:"))
        cll.insertBeforeValue(target, val)
    elif choice == 5:
        cll.deleteStart()
    elif choice == 6:
        cll.deleteEnd()
    elif choice == 7:
        val = int(input("Enter value to delete: "))
        cll.deleteValue(val)
    elif choice == 8:
        cll.traversal()
    elif choice == 9:
        print("Exiting the menu...")
        break
    else:
        print("Invalid choice! Try again.")        
        
# Overview:
# CLL - 8 methods
# insert at start, insert at end, insert after value, insert before value, delete start, delete end, delete by value, traversal

# Node - class, with 2 variables - data, next
# CircularLinkedList class, head = None

# 1) insert start:
# head = None, CLL = empty
# new_node = Node(10) {1000}
# if not head:
# => if not None - T
#       head = new_node => head = 10
#       new_node.next = new_node => 10(None) = 10(1000)
#       Inserted "10" as first node
#   last = head =>  last = 10(1000)
#   while last.next != self.head 
#      => while 10(1000) != 10(1000) - F
#   new_node.next = self.head => new_node.next = 10(1000)
#   last.next = new_node => last.next = 10(1000)
#   self.head = new_node => self.head = 10(1000)
#   print(f"Inserted 10 at start")

# CLL = head -> 10(1000) -> back to head

# 2) Insert start
# new_node = 5 {1500}
# if not self.head 
# => if not 10(1000) - F
# last = self.head => last = 10(1000)
# while last.next != head 
# => while 10(1000) != 10(1000) - F
# new_node.next = self.head => 5(None) = 10(1000) => 5(1000)
# last.next = new_node => 10(1000) = 10(15000)
# self.head = new_node => self.head = 5(1000)
# Inserted 5 at start

# CLL = head -> 5(1000) -> 10(1500) -> back to head

# 3) Insert end
# new_node = 20 {2000}
# if not self.head 
# => if not 5(1000) - F
# last = self.head => last = 5(1000)
# while last.next != head 
# => while 10(1500) != 5(1000) -> T
#       last = last.next => last = 10(1500)
# => while 5(1000) != 5(1000) -> F
# last.next = new_node => 10(1500) = 10(2000)