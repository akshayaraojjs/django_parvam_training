class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def traversal(self):
        current = self.head
        last = None
        print("Forward Traversal")
        while current:
            print(current.data, end=" -> ")
            last = current
            current = current.next
        print("None")
        
        print("Backward Traversal")
        while last:
            print(last.data, end=" -> ")
            last = last.prev
        print("None")
        
    def insertStart(self, value):
        start_node = Node(value) # start_node to add the value at first node
        if self.head is not None:
            start_node.next = self.head
            self.head.prev = start_node
        self.head = start_node
        
    def insertEnd(self, value):
        end_node = Node(value) # end node object to add the value at last node
        if self.head is None:
            self.head = end_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = end_node
        end_node.prev = current
            
    def insertMiddle(self, prev_value, new_value):
        current = self.head
        while current and current.data != prev_value:
            current = current.next
        if not current:
            print(f"Node with data {prev_value} not found!")
            return
        new_node = Node(new_value) # new node object for middle value
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        
dll = DoublyLinkedList()
dll.traversal() # to check whether any elements present in DLL

dll.insertStart(25)
dll.insertStart(50)
dll.traversal()

dll.insertEnd(75)
dll.insertEnd(100)
dll.traversal()

# dll.insertMiddle(75, 85)
# dll.insertMiddle(85, 90)
# dll.traversal()

# Overview:
# Node() => 
# Objects of Node class
# start_node(to add element at first), 
# new_node(add data in between nodes), 
# end_node(to add element at last node)
# 4 methods for Linked List Class: traversal(), insertStart(), insertEnd, insertMiddle()

# Tracing
# dll = Empty, head = None (Because it is empty) 
# 1) insertStart(25)
# start_node = Node(25){1000}
# if self.head is not None:
# => if None is not None: - F
# self.head = start_node => self.head = (None)25(None)

# DLL = (None)25(None)->None, self.head = (None)25(None)
# 2) insertStart(50)
# start_node = Node(50){2000}
# if self.head is not None:
# => if (None)25(None) is not None: - T
#          start_node.next = self.head => start_node.next = 1000
#           self.head.prev = start_node => self.head.prev = (2000)25(None)
# self.head = start_node => self.head = (None)50(1000)

# DLL = (None)50(1000)->(2000)25(None)->None, self.head = (None)50(1000) {2000}
# 3) traversal()
# current = self.head => current = (None)50(1000) {2000}
# last = None
# "Forward Traversal:"
# while current: 
# => while (None)50(1000) - T
#       print(current.data, end="->")
#       => 50 ->
#       last = current => last = (None)50(1000)
#       current = current.next => current = (2000)25(None)
# => while (2000)25(None) - T
#       print(current.data, end="->")
#       => 50 -> 25 ->
#       last = current => last = (2000)25(None)
#       current = current.next => current = None
# => while None - F
#       => 50 -> 25 -> None
# dll = 50 -> 25 -> None

# "Backward Traversal:"
# last = (2000)25(None), current = None
# while last
# => while (2000)25(None) - T
#       print(last.data, end="->")
#       => 25 ->
#       last = last.prev => last = (None)50(1000)
# => while (None)50(1000) - T
#       print(last.data, end="->")
#       => 25 -> 50 ->
#       last = last.prev => last = None
# => while None - F
#       => 25 -> 50 -> None

# dll = (None)50(1000)->(2000)25(None)->None
# head = (None)50(1000) 
# 4) dll.insertEnd(75) 
# end_node = Node(75) {3000}
# if self.head is None:
# => if (None)50(1000) is None - F
# current = self.head => current = (None)50(1000)
# while current.next
# => while (None)50(1000) => while 1000 - T
#       current = current.next => current = (2000)25(None)
# => while (2000)25(None) => while None - F
# current.next = end_node => (2000)25(3000)
# end_node.prev = current => end_node.prev = 1000 => end_node = (1000)75(None)

# dll = (None)50(1000)->(2000)25(3000)->(1000)75(None)->None
# 5) insertEnd(100)
# end_node = Node(1000) {4000}
# head = (None)50(1000)
# if self.head is None:
# => if (None)50(1000) is None - F
# current = self.head => current = (None)50(1000)
# while current.next
# => while (None)50(1000) => while 1000 - T
#       current = current.next => current = (2000)25(None)
# => while (2000)25(3000) => while 3000 - T
#       current = current.next => current = (1000)75(None)
# => while (1000)75(None) => while None - F
# current.next = end_node => (1000)75(4000)
# end_node.prev = current => end_node.prev = 3000 => end_node = (3000)100(None)

# dll = (None)50(1000)->(2000)25(3000)->(1000)75(4000)->(3000)100(None)->None
# head = (None)50(1000)
# 6) insertMiddle(75, 85), prev_data = 75, new_data = 85
# current = self.head => current = (None)50(1000)
# while current & current.data != prev_data 
# => while (None)50(1000) & 50 != 75 => T & T - T
#       current = current.next => current = (2000)25(3000)
# => while (2000)25(3000) & 25 != 75 => T & T - T
#       current = current.next => current = (1000)75(4000)
# => while (1000)75(4000) & 75 != 75 => T & F - F
# if not current:
# => if not (1000)75(4000) - F
# new_node = Node(85) {5000}
# new_node.next = current.next => new_node.next = (None)85(4000)
# new_node.prev = current => new_node.prev = (3000)85(4000) # Got the values for prev and next for new_node
# if current.next
# => if (1000)75(4000) => if 4000
#       current.next.prev = new_node => current.next.prev = {5000}
#       => current.next.prev = (3000)100(None) => (5000)100(None) # Got the prev value for the new_nodes next node
# current.next = new_node => current.next = (1000)75(5000) # Go the next value for new_nodes previous node

# dll = (None)50(1000)->(2000)25(3000)->(1000)75(5000)->(3000)85(4000)->(5000)100(None)->None