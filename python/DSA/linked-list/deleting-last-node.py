class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        
# node1 is an object of Node Class
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)
# 5 objects or 5 nodes

# By default next address will be none as initialized in the constructor
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1
print("Before Deleting:")
while current is not None:
    print(current.data, end = " -> ")
    current = current.next
print("None")

# logic
head = node1
current = head

while current.next.next is not None:
    current = current.next
    
current.next = None

current = head
print("After Deleting:")
while current is not None:
    print(current.data, end = " -> ")
    current = current.next
print("None")

# Tracing:
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# head = current = 10(2000)
# while current.next.next is not None
# => while 2000.next is not None 
# => while 3000 is not None => T
#       current = current.next => current = 20(3000)
# => while 3000.next is not None 
# => while 4000 is not None => T
#       current = current.next => current = 30(4000)
# => while 4000.next is not None 
# => while 5000 is not None => T
#       current = current.next => current = 40(5000)
# => while 5000.next is not None 
# => while None is not None => F
# current.next = None => 40(5000).next = None => current = 40(None)

# printing:
# 10 ->
# 10 -> 20 ->
# 10 -> 20 -> 30 ->
# 10 -> 20 -> 30 -> 40 ->
# 10 -> 20 -> 30 -> 40 -> None