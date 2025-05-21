class TreeNode:
    def __init__(self, value):
        self.value = value            # Value of the node (operand or operator)
        self.left = None              # Left child
        self.right = None             # Right child

def build_expression_tree(postfix_tokens):
    stack = []

    for token in postfix_tokens:
        if token not in "+-*/":
            # Operand: create node and push to stack
            node = TreeNode(token)
            stack.append(node)
        else:
            # Operator: pop two nodes and make them children
            right = stack.pop()
            left = stack.pop()
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.append(node)

    return stack[-1]  # Return the root of the expression tree

def inorder_traversal(root):
    if root is None:
        return ""
    # Recursively get left expression, value, right expression
    return f"({inorder_traversal(root.left)} {root.value} {inorder_traversal(root.right)})"

# ---------- Test Cases Below ----------

# Test Case 1
postfix1 = ["3", "4", "+", "2", "*", "7", "/"]
root1 = build_expression_tree(postfix1)
print("Infix Notation:", inorder_traversal(root1))  # Expected: (((3 + 4) * 2) / 7)

# Test Case 2
postfix2 = ["2", "3", "1", "*", "+", "9", "-"]
root2 = build_expression_tree(postfix2)
print("Infix Notation:", inorder_traversal(root2))  # Expected: ((2 + (3 * 1)) - 9)

# Test Case 3
postfix3 = ["5", "1", "2", "+", "4", "*", "+", "3", "-"]
root3 = build_expression_tree(postfix3)
print("Infix Notation:", inorder_traversal(root3))  # Expected: ((5 + ((1 + 2) * 4)) - 3)
