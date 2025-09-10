# Left-Right Notation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
    
    def add_left(self, child):
        child.parent = self
        self.left = child
    
    def add_right(self, child):
        child.parent = self
        self.right = child
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        indent = "     " * self.get_level()
        prefix = indent + "|--" if self.parent else ""
        print(prefix + str(self.data))
        
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def build_sample_tree(self):
        # Build a sample binary tree
        root = TreeNode("Root")
        
        left_child = TreeNode("Left")
        left_child.add_left(TreeNode("Left-Left"))
        left_child.add_right(TreeNode("Left-Right"))
        
        right_child = TreeNode("Right")
        right_child.add_left(TreeNode("Right-Left"))
        right_child.add_right(TreeNode("Right-Right"))
        
        root.add_left(left_child)
        root.add_right(right_child)
        
        self.root = root
        return root
    
    def build_custom_tree(self, values):
        # Build tree from a list of values (level-order)
        if not values:
            return None
        
        nodes = [TreeNode(val) if val is not None else None for val in values]
        
        for i in range(len(nodes)):
            if nodes[i] is None:
                continue
                
            left_idx = 2 * i + 1
            right_idx = 2 * i + 2
            
            if left_idx < len(nodes) and nodes[left_idx] is not None:
                nodes[i].add_left(nodes[left_idx])
            
            if right_idx < len(nodes) and nodes[right_idx] is not None:
                nodes[i].add_right(nodes[right_idx])
        
        self.root = nodes[0] if nodes else None
        return self.root
    
    def display(self):
        if not self.root:
            print("Tree is empty")
            return
        print("Binary Tree Structure:")
        self.root.print_tree()
    
    def inorder_traversal(self):
        return self._inorder_traversal(self.root)
    
    def _inorder_traversal(self, node):
        if node is None:
            return []
        result = []
        result.extend(self._inorder_traversal(node.left))
        result.append(node.data)
        result.extend(self._inorder_traversal(node.right))
        return result
    
    def preorder_traversal(self):
        return self._preorder_traversal(self.root)
    
    def _preorder_traversal(self, node):
        if node is None:
            return []
        result = []
        result.append(node.data)
        result.extend(self._preorder_traversal(node.left))
        result.extend(self._preorder_traversal(node.right))
        return result
    
    def postorder_traversal(self):
        return self._postorder_traversal(self.root)
    
    def _postorder_traversal(self, node):
        if node is None:
            return []
        result = []
        result.extend(self._postorder_traversal(node.left))
        result.extend(self._postorder_traversal(node.right))
        result.append(node.data)
        return result
    
    def level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = [self.root]
        
        while queue:
            node = queue.pop(0)
            result.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    def get_height(self):
        return self._get_height(self.root)
    
    def _get_height(self, node):
        if node is None:
            return 0
        return 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    def count_nodes(self):
        return self._count_nodes(self.root)
    
    def _count_nodes(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)
    
    def find_node(self, data):
        return self._find_node(data, self.root)
    
    def _find_node(self, data, node):
        if node is None:
            return None
        if node.data == data:
            return node
        
        left_result = self._find_node(data, node.left)
        if left_result:
            return left_result
            
        return self._find_node(data, node.right)
    
    def add_node(self, parent_data, child_data, position='left'):
        parent_node = self.find_node(parent_data)
        if not parent_node:
            print(f"Parent node '{parent_data}' not found")
            return False
        
        new_node = TreeNode(child_data)
        
        if position == 'left':
            if parent_node.left:
                print(f"Parent '{parent_data}' already has a left child")
                return False
            parent_node.add_left(new_node)
        elif position == 'right':
            if parent_node.right:
                print(f"Parent '{parent_data}' already has a right child")
                return False
            parent_node.add_right(new_node)
        else:
            print("Position must be 'left' or 'right'")
            return False
        
        return True


# Demonstration
if __name__ == "__main__":
    # Create a binary tree
    tree = BinaryTree()
    
    # Build a sample tree
    tree.build_sample_tree()
    
    print("Binary Tree Structure:")
    tree.display()
    
    print("\n" + "="*50)
    print("Tree Analysis:")
    print("="*50)
    
    # Tree traversals
    print("Inorder Traversal:", tree.inorder_traversal())
    print("Preorder Traversal:", tree.preorder_traversal())
    print("Postorder Traversal:", tree.postorder_traversal())
    print("Level-order Traversal:", tree.level_order_traversal())
    
    # Tree properties
    print("Tree Height:", tree.get_height())
    print("Total Nodes:", tree.count_nodes())
    
    # Add a new node
    print("\nAdding new node 'Left-Left-Left' to 'Left-Left'...")
    tree.add_node("Left-Left", "Left-Left-Left", 'left')
    
    print("\nUpdated Tree Structure:")
    tree.display()
    
    # Add another node
    print("\nAdding new node 'Left-Left-Right' to 'Left-Left'...")
    tree.add_node("Left-Left", "Left-Left-Right", 'right')
    
    print("\nFinal Tree Structure:")
    tree.display()
    
    # Show updated properties
    print("\nUpdated Tree Height:", tree.get_height())
    print("Updated Total Nodes:", tree.count_nodes())
    
    # Build a custom tree from a list
    print("\n\n" + "="*60)
    print("Custom Binary Tree from List:")
    print("="*60)
    
    # None values represent empty nodes
    custom_values = ["A", "B", "C", "D", "E", None, "F", None, "G", "H"]
    custom_tree = BinaryTree()
    custom_tree.build_custom_tree(custom_values)
    
    custom_tree.display()
    
    print("Inorder Traversal:", custom_tree.inorder_traversal())
    print("Level-order Traversal:", custom_tree.level_order_traversal())
    print("Tree Height:", custom_tree.get_height())
    print("Total Nodes:", custom_tree.count_nodes())


# Example of a more complex binary tree
def build_expression_tree():
    print("\n\n" + "="*60)
    print("Expression Tree Example:")
    print("="*60)
    
    # Build a binary tree for expression: (a + b) * (c - d)
    expr_tree = BinaryTree()
    root = TreeNode("*")
    
    plus = TreeNode("+")
    plus.add_left(TreeNode("a"))
    plus.add_right(TreeNode("b"))
    
    minus = TreeNode("-")
    minus.add_left(TreeNode("c"))
    minus.add_right(TreeNode("d"))
    
    root.add_left(plus)
    root.add_right(minus)
    
    expr_tree.root = root
    expr_tree.display()
    
    print("Inorder Traversal (Infix):", expr_tree.inorder_traversal())
    print("Preorder Traversal (Prefix):", expr_tree.preorder_traversal())
    print("Postorder Traversal (Postfix):", expr_tree.postorder_traversal())
    
    return expr_tree


# Run the expression tree example
expression_tree = build_expression_tree()