class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

def range_values_in_bst(root, min_val, max_val):
    result = []

    def inorder(node):
        if not node:
            return
        if node.val > min_val:
            inorder(node.left)
        if min_val <= node.val <= max_val:
            result.append(node.val)
        if node.val < max_val:
            inorder(node.right)

    inorder(root)
    return result

# Helper function to insert values into BST
def insert_bst(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.val:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

# Building the BST
values = [20, 10, 5, 15, 30, 25, 35]
root = None
for val in values:
    root = insert_bst(root, val)

# Test 1: Range [10, 30]
print(range_values_in_bst(root, 10, 30))  
# Expected Output: [10, 15, 20, 25, 30]

# Test 2: Range [5, 15]
print(range_values_in_bst(root, 5, 15))  
# Expected Output: [5, 10, 15]

# Test 3: Range [25, 40]
print(range_values_in_bst(root, 25, 40))  
# Expected Output: [25, 30, 35]

# Test 4: Range [0, 4]
print(range_values_in_bst(root, 0, 4))  
# Expected Output: []

# Test 5: Range [20, 20]
print(range_values_in_bst(root, 20, 20))  
# Expected Output: [20]
