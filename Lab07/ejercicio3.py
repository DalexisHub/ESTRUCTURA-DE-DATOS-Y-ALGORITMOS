class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def mirror_tree(root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    mirror_tree(root.left)
    mirror_tree(root.right)
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

# Crear el árbol original
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("In-order traversal before mirroring:")
in_order_traversal(root)  # Output: 4 2 5 1 3
print("\n")

# Aplicar espejo
mirror_tree(root)

print("In-order traversal after mirroring:")
in_order_traversal(root)  # Output: 3 1 5 2 4
print()

#-----TEST CASES----
 
# Test Case 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.left = TreeNode(4)
root1.left.right = TreeNode(5)

print("In-order before mirroring:")
in_order_traversal(root1)
mirror_tree(root1)
print("\nIn-order after mirroring:")
in_order_traversal(root1)
print("\n")  # Expected Output: 3 1 5 2 4

# Test Case 2
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)

print("In-order before mirroring:")
in_order_traversal(root2)
mirror_tree(root2)
print("\nIn-order after mirroring:")
in_order_traversal(root2)
print("\n")  # Expected Output: 30 10 20

# Test Case 3 (Single Node)
root3 = TreeNode(99)

print("In-order before mirroring:")
in_order_traversal(root3)
mirror_tree(root3)
print("\nIn-order after mirroring:")
in_order_traversal(root3)
print("\n")  # Expected Output: 99
