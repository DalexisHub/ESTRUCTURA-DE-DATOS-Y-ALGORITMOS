class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root, val1, val2):
    current = root
    while current:
        if val1 < current.val and val2 < current.val:
            current = current.left
        elif val1 > current.val and val2 > current.val:
            current = current.right
        else:
            return current.val
        
        # Construct BST manually
root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

print(lowest_common_ancestor(root, 2, 8))  # Output: 6

print(lowest_common_ancestor(root, 2, 4))  # Output: 2

print(lowest_common_ancestor(root, 3, 5))  # Output: 4
