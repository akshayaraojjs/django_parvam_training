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
print("Before Insertion:")
while current is not None:
    print(current.data, end = " -> ")
    # print(current.data, current.next, end = " -> ")
    current = current.next
print("None")

new_node = Node(25)
current = node1
while current is not None and current.data != 20:
    current = current.next
new_node.next = current.next
current.next = new_node    

current = node1
print("After Insertion:")
while current is not None:
    print(current.data, end = " -> ")
    # print(current.data, current.next, end = " -> ")
    current = current.next
print("None")

# Tracing:
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# current = 10(2000), new_node = 25(None)
# while current is not None and current.data != 20
# => while 10(2000) is not None and 10 != 20 => T & T => T
#       current = current.next => current = 20(3000)
# => while 20(3000) is not None and 20 != 20 => T & F => F
# new_node.next = current.next => 25(None) = (3000) => new_node.next = 25(3000)
# current.next = new_node => 20(3000) = (2500) => current.next = 20(2500)

# printing:
#  10 ->
#  10 -> 20 ->
#  10 -> 20 -> 25 ->
#  10 -> 20 -> 25 -> 30 ->
#  10 -> 20 -> 25 -> 30 -> 40 ->
#  10 -> 20 -> 25 -> 30 -> 40 -> 50 ->
#  10 -> 20 -> 25 -> 30 -> 40 -> 50 -> None