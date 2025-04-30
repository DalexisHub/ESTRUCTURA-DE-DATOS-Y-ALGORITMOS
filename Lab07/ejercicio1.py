class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def tree_height(root):
    if root is None:
        return -1  # height of empty tree is -1 (0 edges)
    left_height = tree_height(root.left)
    right_height = tree_height(root.right)
    return 1 + max(left_height, right_height)

# Árbol de ejemplo:
#      1
#     / \
#    2   3
#   / \
#  4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Altura del árbol:", tree_height(root))  # Salida esperada: 2

# Pruebita 1
print(tree_height(None)) 
# Pruebita 2
root = TreeNode(10)
print(tree_height(root))  
# Pruebita 3
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
print(tree_height(root))  

