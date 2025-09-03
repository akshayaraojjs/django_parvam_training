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

new_node = Node(60) # new object or new node
print(new_node.data)
print(new_node.next)
head = node1
current = head

while current.next is not None:
    current = current.next
current.next = new_node

current = node1
while current is not None:
    print(current.data, end = " -> ")
    # To check the address of the next node in hex format
    # print(current.data,current.next, end = " -> ")
    current = current.next
print("None")

# Tracing:
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# head = current = 10(2000) (Node1), new_node = 60(None)
# while current.next is not None:
# => while 2000 is not None: => T
#       current = current.next => current = 20(3000)
# => while 3000 is not None: => T
#       current = current.next => current = 30(4000)
# => while 4000 is not None: => T
#       current = current.next => current = 40(5000)
# => while 5000 is not None: => T
#       current = current.next => current = 50(None)
# => while None is not None: => F
# current.next = new_node
# => 50(None) = 6000 => 50(6000)

# printing
# 10 ->
# 10 -> 20 ->
# 10 -> 20 -> 30 ->
# 10 -> 20 -> 30 -> 40 ->
# 10 -> 20 -> 30 -> 40 -> 50 ->
# 10 -> 20 -> 30 -> 40 -> 50 -> 60 ->
# 10 -> 20 -> 30 -> 40 -> 50 -> 60 -> None