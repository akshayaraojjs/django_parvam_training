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
while current.next.data != 30:
    current = current.next
current.next = current.next.next

current = node1
print("After Deleting:")
while current is not None:
    print(current.data, end = " -> ")
    current = current.next
print("None")

# Tracing:
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# head = current = 10(2000)
# while current.next.data != 30
# => while 10(2000).next.data != 30
# => while 10(2000).(3000).data != 30
# => while 10(2000).(3000).20 != 30
# => while 20 != 30 = > T
#       current = current.next => current = 20(3000)
# => while 20(3000).next.data != 30
# => while 20(3000).(4000).data != 30
# => while 20(3000).(4000).30 != 30
# => while 30 != 30 = > F
# current.next = current.next.next
# => 20(3000) = (4000) => current.next = 20(4000) 

# printing:
# 10 ->
# 10 -> 20 ->
# 10 -> 20 -> 40 ->
# 10 -> 20 -> 40 -> 50 ->
# 10 -> 20 -> 40 -> 50 -> None


# double linked list
# (None)10(2000), (1000)20(3000), (2000)30(4000), (3000)40(5000), (4000)50(None)

# circular linked list
# 10(2000), 20(3000), 30(4000), 40(5000), 50(1000)

# doubly circular linked list
# (5000)10(2000), (1000)20(3000), (2000)30(4000), (3000)40(5000), (4000)50(1000)