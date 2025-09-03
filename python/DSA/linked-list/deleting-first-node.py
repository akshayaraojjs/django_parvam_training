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
if head is not None:
    head = head.next

current = head
print("After Deleting:")
while current is not None:
    print(current.data, end = " -> ")
    current = current.next
print("None")

# Tracing:
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# head = 10(2000)
# if head is not None
# => if 10(2000) is not None => T
#       head = head.next => head = 20(3000)

# printing:
# 20 ->
# 20 -> 30 ->
# 20 -> 30 -> 40 ->
# 20 -> 30 -> 40 -> 50 ->
# 20 -> 30 -> 40 -> 50 -> None