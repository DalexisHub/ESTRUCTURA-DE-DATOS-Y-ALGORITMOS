class GenericTreeNode:
    """Node for a generic tree"""
    def __init__(self, value):
        self.value = value
        self.children = []

class GenericTree:
    """Generic tree implementation"""
    
    def __init__(self, root=None):
        self.root = root
    
    def height(self):
        """Calculate tree height"""
        def recursive_height(node):
            if node is None:
                return 0
            if not node.children:
                return 1
            return 1 + max(recursive_height(child) for child in node.children)
        
        return recursive_height(self.root)

# ✅ Test cases
# Test 1: Empty tree
empty_tree = GenericTree(None)
print(empty_tree.height() == 0)  # 📭 Empty tree

# Test 2: Single node
single = GenericTree(GenericTreeNode('A'))
print(single.height() == 1)  # 🌱 Single node

# Test 3: Linear tree: A → B → C
linear_root = GenericTreeNode('A')
linear_b = GenericTreeNode('B')
linear_c = GenericTreeNode('C')
linear_root.children = [linear_b]
linear_b.children = [linear_c]
linear_tree = GenericTree(linear_root)
print(linear_tree.height() == 3)  # 📏 Linear path
