"""Expression tree traversal module."""

class TreeNode:
    """Node of a binary expression tree."""
    def __init__(self, value):
        """Initialize a tree node with a value."""
        self.value = value  # Store the value of the node (operand/operator)
        self.left = None    # Left child
        self.right = None   # Right child

def inorder_traversal(root):
    """Return inorder (infix) traversal of the tree as a list."""
    if root is None:
        return []
    return (inorder_traversal(root.left) +
            [root.value] +
            inorder_traversal(root.right))

def preorder_traversal(root):
    """Return preorder (prefix) traversal of the tree as a list."""
    if root is None:
        return []
    return ([root.value] +
            preorder_traversal(root.left) +
            preorder_traversal(root.right))

def postorder_traversal(root):
    """Return postorder (postfix) traversal of the tree as a list."""
    if root is None:
        return []
    return (postorder_traversal(root.left) +
            postorder_traversal(root.right) +
            [root.value])

# Build an example expression tree: (a + b) * (c - d)
root_main = TreeNode('*')
root_main.left = TreeNode('+')
root_main.right = TreeNode('-')
root_main.left.left = TreeNode('a')
root_main.left.right = TreeNode('b')
root_main.right.left = TreeNode('c')
root_main.right.right = TreeNode('d')

print("Inorder Traversal (Infix):", inorder_traversal(root_main))
print("Preorder Traversal (Prefix):", preorder_traversal(root_main))
print("Postorder Traversal (Postfix):", postorder_traversal(root_main))

print("=== Test Case 1: (a + b) * (c - d) ===")
root1 = TreeNode('*')
root1.left = TreeNode('+')
root1.right = TreeNode('-')
root1.left.left = TreeNode('a')
root1.left.right = TreeNode('b')
root1.right.left = TreeNode('c')
root1.right.right = TreeNode('d')

print("Inorder Traversal:", inorder_traversal(root1))
print("Preorder Traversal:", preorder_traversal(root1))
print("Postorder Traversal:", postorder_traversal(root1))

print("=== Test Case 2: a + (b * c) ===")
root2 = TreeNode('+')
root2.left = TreeNode('a')
root2.right = TreeNode('*')
root2.right.left = TreeNode('b')
root2.right.right = TreeNode('c')

print("Inorder Traversal:", inorder_traversal(root2))
print("Preorder Traversal:", preorder_traversal(root2))
print("Postorder Traversal:", postorder_traversal(root2))