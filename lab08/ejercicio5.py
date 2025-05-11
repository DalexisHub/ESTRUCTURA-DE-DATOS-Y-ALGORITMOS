class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def prune_tree(root, target):
    if not root:
        return None

    root.left = prune_tree(root.left, target)
    root.right = prune_tree(root.right, target)

    if root.val != target and not root.left and not root.right:
        return None

    return root

def print_tree_preorder(root):
    if not root:
        return
    print(root.val, end=' ')
    print_tree_preorder(root.left)
    print_tree_preorder(root.right)

# Test Case 1
print("Test Case 1:")
root1 = TreeNode(1,
    TreeNode(0, TreeNode(0), TreeNode(0)),
    TreeNode(1)
)
target1 = 1
pruned1 = prune_tree(root1, target1)
print("Pruned Tree (preorder):")
print_tree_preorder(pruned1)  # Expected: 1 1

print("\n" + "-"*30)

# Test Case 2
print("Test Case 2:")
root2 = TreeNode(2, TreeNode(2), TreeNode(2))
target2 = 2
pruned2 = prune_tree(root2, target2)
print("Pruned Tree (preorder):")
print_tree_preorder(pruned2)  # Expected: 2 2 2

print("\n" + "-"*30)

# Test Case 3
print("Test Case 3:")
root3 = TreeNode(0, TreeNode(0), TreeNode(0))
target3 = 1
pruned3 = prune_tree(root3, target3)
print("Pruned Tree (preorder):")
print_tree_preorder(pruned3)  # Expected: (nothing, everything is pruned)
