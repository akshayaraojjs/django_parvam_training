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
        
    def deleteStart(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        print(f"Deleting {self.head.data} from first node")
        self.head = self.head.next
        if self.head:
            self.head.prev = None
            
    def deleteEnd(self):
        if self.head is None:
            print("Linked List is Empty!")
            return
        current = self.head
        if current.next is None:
            print(f"Deleting {current.data} (only node)")
            self.head = None
            return
        while current.next:
            current = current.next
        print(f"Deleting {current.data} from last node")
        current.prev.next = None
        
    def deleteByValue(self, value):
        if self.head is None:
            print("Linked List is Empty!")
            return
        current = self.head
        while current and current.data != value:
            current = current.next
        if not current:
            print(f"Node with data {value} not found!")
            return
        print(f"Deleting {current.data} from middle")
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
            
dll = DoublyLinkedList()
dll.traversal() # to check whether any elements present in DLL

dll.insertEnd(25)
dll.insertEnd(50)
dll.insertEnd(75)
dll.insertEnd(100)
dll.insertEnd(125)
dll.traversal()

dll.deleteStart()
dll.traversal()

dll.deleteEnd()
dll.traversal()

dll.deleteByValue(75)
dll.traversal()

# Overview:
# Node() => 
# Objects of Node class
# start_node(to add element at first), 
# new_node(add data in between nodes), 
# end_node(to add element at last node)
# 4 methods for Linked List Class: traversal(), insertStart(), insertEnd, insertMiddle()