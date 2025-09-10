# Only Traversal
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # Inorder Traversal (Left → Root → Right)
    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.key, end=" ")
            self.inorder(node.right)

    # Preorder Traversal (Root → Left → Right)
    def preorder(self, node):
        if node:
            print(node.key, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    # Postorder Traversal (Left → Right → Root)
    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key, end=" ")


# Usage
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print("Inorder Traversal:")
tree.inorder(tree.root)   # 4 2 5 1 3

print("\nPreorder Traversal:")
tree.preorder(tree.root)  # 1 2 4 5 3

print("\nPostorder Traversal:")
tree.postorder(tree.root) # 4 5 2 3 1

from collections import deque

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.key, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

print("\nLevel Order Traversal:")
level_order(tree.root)  # 50 30 70 20 40 60 80