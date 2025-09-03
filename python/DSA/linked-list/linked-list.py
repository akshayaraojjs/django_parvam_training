# Traversal of Linked List
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

# Traversal or Printing the Linked List
current = node1
while current is not None:
    print(current.data, end = " -> " )
    current = current.next
print("None")

# Tracing:
# Node1 = 10(2000) => data - 10, next - 2000 
# 10(2000), 20(3000), 30(4000), 40(5000), 50(None) => 5 data & address
# current = 10(2000) is not None => T
    # 10 -> 
    # current = 20(3000) # Shifting the current node
# current = 20(3000) is not None => T
    # 10 -> 20 ->
    # current = 30(4000) # Shifting the current node
# current = 30(4000) is not None => T
    # 10 -> 20 -> 30 -> 
    # current = 40(5000) # Shifting the current node
# current = 40(5000) is not None => T
    # 10 -> 20 -> 30 -> 40 ->
    # current = 50(None) # Shifting the current node
# current = 50(None) is not None => T
    # 10 -> 20 -> 30 -> 40 -> 50 -> 
    # current = None # Shifting the current node
# current = None is not None => F
    # 10 -> 20 -> 30 -> 40 -> 50 -> None