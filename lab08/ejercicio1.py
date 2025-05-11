# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Step 1: Perform inorder traversal and collect nodes
def inorder_traversal(root, nodes):
    if root:
        inorder_traversal(root.left, nodes)
        nodes.append(root)
        inorder_traversal(root.right, nodes)

# Step 2: Build balanced BST from sorted nodes
def build_balanced_bst(nodes, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    root = nodes[mid]
    root.left = build_balanced_bst(nodes, start, mid - 1)
    root.right = build_balanced_bst(nodes, mid + 1, end)
    return root

# Step 3: Main function
def balance_bst(root):
    nodes = []
    inorder_traversal(root, nodes)
    return build_balanced_bst(nodes, 0, len(nodes) - 1)

# Helper to print tree in level order (for visual validation)
from collections import deque
def print_level_order(root):
    if not root:
        return "[]"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val if node else None)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return result

# Test Case 1: Unbalanced BST (skewed right)
root1 = TreeNode(1)
root1.right = TreeNode(2)
root1.right.right = TreeNode(3)
root1.right.right.right = TreeNode(4)

balanced1 = balance_bst(root1)
print("Balanced Tree Level Order:", print_level_order(balanced1))
# Expected output: Balanced tree like [2, 1, 3, None, None, None, 4]

# Test Case 2: Already Balanced BST
root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)

balanced2 = balance_bst(root2)
print("Balanced Tree Level Order:", print_level_order(balanced2))
# Expected output: [2, 1, 3]

# Test Case 3: Single node
root3 = TreeNode(10)
balanced3 = balance_bst(root3)
print("Balanced Tree Level Order:", print_level_order(balanced3))
# Expected output: [10]
