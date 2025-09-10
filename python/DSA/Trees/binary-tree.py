# Traversal with Tree Structure
class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    # Pre-order, Inorder & Post-order traveral uses Stack
    # Pre-order Traversal
    def preorder_traversal(self, node):
        if node:
            print(node.data, end = " ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
            
    # Inorder Traversal
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end = " ")
            self.inorder_traversal(node.right)
    
    # Post-order Traversal
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end = " ")
    
    # For level-order traversal, we will use Queue
    def levelorder_traversal(self):
        if not self.root:
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.data, end = " ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
    def display(self):
        if not self.root:
            print("Tree is empty")
            return
            
        lines, _, _, _ = self._display_aux(self.root)
        for line in lines:
            print(line)
    
    def _display_aux(self, node):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child
        if node.right is None and node.left is None:
            line = str(node.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child
        if node.right is None:
            lines, n, p, x = self._display_aux(node.left)
            s = str(node.data)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child
        if node.left is None:
            lines, n, p, x = self._display_aux(node.right)
            s = str(node.data)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self._display_aux(node.left)
        right, m, q, y = self._display_aux(node.right)
        s = str(node.data)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
                
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print("Tree Structure:")
tree.display()

print("Pre-order Traversal:")
tree.preorder_traversal(tree.root)

print("\nInorder Traversal:")
tree.inorder_traversal(tree.root)

print("\nPost-order Traversal:")
tree.postorder_traversal(tree.root)

print("\nLevel-order Traversal:")
tree.levelorder_traversal()