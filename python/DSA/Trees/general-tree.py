class TreeNode:
    def __init__(self, value):
        # data, children, parent
        self.data = value
        self.children = []
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            # 1st iteration: level = level + 1 = 0 + 1 = 1
            # 2nd iteration: level = level + 1 = 1 + 1 = 2
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spacing = "      " * self.get_level()
        # Ternary Operator
        # prefix = spacing + "|---" if self.parent else ""
        if self.parent:
            prefix = spacing + "|---"
        else:
            prefix = ""
        print(prefix + str(self.data))
        
        # Recursion: calling the function itself
        if self.children:
            for child in self.children:
                child.print_tree()
        
class GeneralTree:
    def __init__(self):
        self.root = None
        
    def build_tree(self):
        # Root Node
        # [10, 20, 30, 40, 50, 60, 70, 80, 55, 65, 75, 85, 95]
        root = TreeNode(10) # object of TreeNode
        
        child1 = TreeNode(20)
        child1.add_child(TreeNode(30))
        child1.add_child(TreeNode(40))
        child1.add_child(TreeNode(50))
        
        child2 = TreeNode(60)
        child2.add_child(TreeNode(70))
        child2.add_child(TreeNode(80))
        
        child3 = TreeNode(55)
        child3.add_child(TreeNode(65))
        child3.add_child(TreeNode(75))
        child3.add_child(TreeNode(85))
        child3.add_child(TreeNode(95))
        
        root.add_child(child1)
        root.add_child(child2)
        root.add_child(child3)
        
        self.root = root
        return root
    
    def display(self):
        if not self.root:
            print("Tree is Empty")
            return
        self.root.print_tree()
        
        
tree = GeneralTree() #Object of General Tree class

tree.build_tree()
# When we call display() method, it will call print_tree() method and it is going to call back the get_level() method
# display() -> print_tree() -> get_level()
tree.display()

        # Complex Tree Structure
#                    10
#       20           60            55   
#   30  40  50    70    80   65  75  85  95

# Printing the Tree
# 10
# |---20
#     |---30
#     |---40
#     |---50
# |---60
#     |---70
#     |---80
# |---55
#     |---65
#     |---75
#     |---85
#     |---95

# Tracing:
# 
# root = TreeNode(10)
# root.data = 10, root.children = [], root.parent = None

# child1 = TreeNode(20)
# child1.data = 20, child1.children = [], child1.parent = None

# child1.add_child(TreeNode(30))
# child1.one.data = 30, child1.one.children = [], child1.one.parent = child1

# add_child(self, child)
# child.parent = self
# self.children.append(child)

# child1.add_child(child1, one = 30)
# one.parent = child1
# child1.children.append(one) => child1.children = [30]

# child1.add_child(TreeNode(40))
# child1.two.data = 30, child1.two.children = [], child1.two.parent = child1

# child1.add_child(child1, two = 40)
# two.parent = child1
# child1.children.append(two) => child1.children = [30, 40]

# child1.add_child(TreeNode(50))
# child1.three.data = 40, child1.three.children = [], child1.three.parent = child1

# child1.add_child(child1, three = 50)
# three.parent = child1
# child1.children.append(three) => child1.children = [30, 40, 50]

# child1.children = [30, 40, 50]


# child2 = TreeNode(60)
# child2.data = 60, child2.children = [], child2.parent = None

# child2.add_child(TreeNode(70))
# child2.one.data = 70, child2.one.children = [], child2.one.parent = None

# child2.add_child(child2, one = 70)
# one.parent = child2
# child2.children.append(one) => child2.children = [70]

# child2.add_child(TreeNode(80))
# child2.two.data = 80, child2.two.children = [], child2.one.parent = None

# child2.add_child(child2, two = 80)
# two.parent = child2
# child2.children.append(two) => child2.children = [70, 80]

# child2.children = [70, 80]
# child2 = TreeNode(60)


# child3.data = 55, child3.children = [], child2.parent = None

# child3.add_child(TreeNode(65))
# child3.one.data = 65, child3.one.children = [], child3.one.parent = None

# child3.add_child(child3, one = 65)
# one.parent = child3
# child3.children.append(one) => child3.children = [65]

# child3.add_child(TreeNode(75))
# child3.two.data = 75, child3.two.children = [], child3.two.parent = None

# child3.add_child(child3, two = 75)
# two.parent = child3
# child3.children.append(two) => child3.children = [65, 75]

# child3.add_child(TreeNode(85))
# child3.three.data = 85, child3.three.children = [], child3.three.parent = None

# child3.add_child(child3, three = 85)
# three.parent = child3
# child3.children.append(three) => child3.children = [65, 75, 85]

# child3.add_child(TreeNode(95))
# child3.four.data = 85, child3.four.children = [], child3.four.parent = None

# child3.add_child(child3, four = 95)
# four.parent = child3
# child3.children.append(four) => child3.children = [65, 75, 85, 95]

# child3.children = [65, 75, 85, 95]

# root.add_child(child1)
# root.children = [child1]
# child1.parent = root
# root.add_child(child2)
# root.children = [child1, child2]
# child2.parent = root
# root.add_child(child3)
# root.children = [child1, child2, child3]
# child3.parent = root


# Final:
# root = 10, child1 = 20, child2 = 60, child3 = 55
# root.children = [child1, child2, child3]
# child1.children = [30, 40, 50]
# child2.children = [70, 80]
# child3.children = [65, 75, 85, 95]