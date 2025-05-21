class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value  # Can be int or operator: '+', '-', '*', '/'
        self.left = left
        self.right = right

def evaluate_expression_tree(node):
    if node is None:
        return 0

    # If it's a leaf node (integer), return its value
    if node.left is None and node.right is None:
        return int(node.value)

    # Recursively evaluate left and right subtrees
    left_val = evaluate_expression_tree(node.left)
    right_val = evaluate_expression_tree(node.right)

    # Apply the operator at the current node
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        # Handle division (float result)
        return left_val / right_val
    else:
        raise ValueError(f"Unknown operator: {node.value}")

#TEST CASES

# Tree: ((3 + 2) * (4 - 1))
#         *
#       /   \
#     +       -
#    / \     / \
#   3   2   4   1

tree = TreeNode('*',
    TreeNode('+', TreeNode(3), TreeNode(2)),
    TreeNode('-', TreeNode(4), TreeNode(1))
)
print(evaluate_expression_tree(tree))

# Tree: (7 + ((3 * 2) / 6))
#        +
#      /   \
#     7     /
#         /   \
#        *     6
#       / \
#      3   2

tree2 = TreeNode('+',
    TreeNode(7),
    TreeNode('/',
        TreeNode('*', TreeNode(3), TreeNode(2)),
        TreeNode(6)
    )
)
print(evaluate_expression_tree(tree2))

# Tree: (10 / (2 + 3))
#         /
#       /   \
#     10     +
#           / \
#          2   3

tree3 = TreeNode('/',
    TreeNode(10),
    TreeNode('+', TreeNode(2), TreeNode(3))
)
print(evaluate_expression_tree(tree3))
