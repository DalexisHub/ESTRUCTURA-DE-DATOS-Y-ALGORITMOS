class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    def inorder(node):
        nonlocal count, result
        if not node or result is not None:
            return
        inorder(node.left)
        count += 1
        if count == k:
            result = node.val
            return
        inorder(node.right)
    
    count = 0
    result = None
    inorder(root)
    return result

# Helper function to insert nodes into the BST
def insert(root, val):
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Test Case 1
root1 = None
for val in [5, 3, 6, 2, 4, 1]:
    root1 = insert(root1, val)
print(kth_smallest(root1, 3))  # Expected output: 3

# Test Case 2
root2 = None
for val in [10, 5, 15, 3, 7, 12, 18]:
    root2 = insert(root2, val)
print(kth_smallest(root2, 5))  # Expected output: 12

# Test Case 3
root3 = TreeNode(1)
print(kth_smallest(root3, 1))  # Expected output: 1
