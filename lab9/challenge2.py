class Node:
    """A node in the expression tree."""
    def __init__(self, value):
        self.value = value      # Operator or operand
        self.left = None        # Left child
        self.right = None       # Right child

class ExpressionTree:
    """Expression tree implementation"""

    def __init__(self):
        self.root = None  # Root of the tree

    @classmethod
    def from_infix(cls, tokens):
        """Build expression tree from infix notation"""

        def precedence(op):
            """Return the precedence of an operator"""
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0  # For '('

        def is_operator(token):
            """Check if the token is an operator"""
            return token in '+-*/'

        def to_postfix(infix_tokens):
            """Convert infix tokens to postfix (Reverse Polish Notation) using Shunting Yard algorithm"""
            output = []          # Postfix output
            stack = []           # Operator stack

            for token in infix_tokens:
                if token.isalnum():  # Operand (number or variable)
                    output.append(token)
                elif token == '(':
                    stack.append(token)
                elif token == ')':
                    # Pop until '(' is found
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()  # Remove '('
                elif is_operator(token):
                    # Pop operators with higher or equal precedence
                    while stack and precedence(stack[-1]) >= precedence(token):
                        output.append(stack.pop())
                    stack.append(token)

            # Pop remaining operators
            while stack:
                output.append(stack.pop())

            return output

        def build_tree(postfix_tokens):
            """Build expression tree from postfix expression"""
            stack = []

            for token in postfix_tokens:
                node = Node(token)
                if is_operator(token):
                    # Pop right and left children from stack
                    node.right = stack.pop()
                    node.left = stack.pop()
                # Push current node to stack
                stack.append(node)

            return stack[-1]  # Root node

        # Convert infix to postfix
        postfix = to_postfix(tokens)

        # Build the tree from postfix
        tree = cls()
        tree.root = build_tree(postfix)
        return tree


# ✅ Test cases
# Test 1: Simple addition
# Input: 2 + 3
# Tree:    +
#         / \
#        2   3
tree1 = ExpressionTree.from_infix(['2', '+', '3'])
print(tree1.root.value == '+' and tree1.root.left.value == '2' and tree1.root.right.value == '3')  # 🌱 Simple tree

# Test 2: Operator precedence
# Input: 2 + 3 * 4
# Tree:    +
#         / \
#        2   *
#           / \
#          3   4
tree2 = ExpressionTree.from_infix(['2', '+', '3', '*', '4'])
print(tree2.root.value == '+' and tree2.root.right.value == '*')  # 📊 Precedence structure

# Test 3: Parentheses change structure
# Input: (2 + 3) * 4
# Tree:    *
#         / \
#        +   4
#       / \
#      2   3
tree3 = ExpressionTree.from_infix(['(', '2', '+', '3', ')', '*', '4'])
print(tree3.root.value == '*' and tree3.root.left.value == '+')  # 🔗 Parentheses effect

# Test 4: Variables in expression
# Input: x + y * z
# Tree:    +
#         / \
#        x   *
#           / \
#          y   z
tree4 = ExpressionTree.from_infix(['x', '+', 'y', '*', 'z'])
print(tree4.root.value == '+' and tree4.root.right.value == '*')  # 🔤 Variable tree

# Test 5: Complex nested expression
# Input: (a + b) / (c - d)
# Tree:      /
#          /   \
#         +     -
#        / \   / \
#       a   b c   d
tree5 = ExpressionTree.from_infix(['(', 'a', '+', 'b', ')', '/', '(', 'c', '-', 'd', ')'])
print(tree5.root.value == '/' and tree5.root.left.value == '+' and tree5.root.right.value == '-')  # 🧮 Complex tree
