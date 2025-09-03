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

new_node = Node(35)
head = node1
new_node.next = head
head = new_node

current = head
while current is not None:
    print(current.data, end = " -> ")
    current = current.next
print("None")

# Tracing:
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# head = 10(2000), new_node = 35(None)
# new_node.next = head => new_node.next = 10(2000) => new_node.next = 35(1000)
# head = new_node => head = 35(1000)

# printing:
# 35 ->
# 35 -> 10 ->
# 35 -> 10 -> 20 ->
# 35 -> 10 -> 20 -> 30 -> 
# 35 -> 10 -> 20 -> 30 -> 40 ->
# 35 -> 10 -> 20 -> 30 -> 40 -> 50 ->
# 35 -> 10 -> 20 -> 30 -> 40 -> 50 -> None