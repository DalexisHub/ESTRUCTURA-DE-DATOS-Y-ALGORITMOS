# --- Tree node definition ---
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Main function to validate BST ---
def is_valid_bst(root):
    """Checks if a binary tree is a valid Binary Search Tree (BST)."""
    def validate(node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (
            validate(node.left, min_val, node.val) and
            validate(node.right, node.val, max_val)
        )
    return validate(root, float('-inf'), float('inf'))

# --- Helper function to build tree from level-order list ---
def build_tree(values):
    """Builds a complete binary tree from a list (level-order traversal)."""
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i in range(len(nodes)):
        if nodes[i]:
            left_i = 2 * i + 1
            right_i = 2 * i + 2
            if left_i < len(nodes):
                nodes[i].left = nodes[left_i]
            if right_i < len(nodes):
                nodes[i].right = nodes[right_i]
    return nodes[0]

# --- Invalid BST trees for specific test cases ---
def build_invalid_tree1():
    # Invalid BST: left child > root
    #     5
    #    / \
    #   6   7
    return TreeNode(5, TreeNode(6), TreeNode(7))

def build_invalid_tree2():
    # Invalid BST: right child < root
    #     5
    #    / \
    #   3   4
    return TreeNode(5, TreeNode(3), TreeNode(4))

# --- Test cases ---
print("✅ Test 1: Valid BST")
#     5
#    / \
#   3   7
#  / \ / \
# 2  4 6  8
print(is_valid_bst(build_tree([5, 3, 7, 2, 4, 6, 8])) == True)

print("Test 2: Invalid BST - left violation")
print(is_valid_bst(build_invalid_tree1()) == False)

print("Test 3: Invalid BST - right violation")
print(is_valid_bst(build_invalid_tree2()) == False)

print("Test 4: Single node")
print(is_valid_bst(build_tree([42])) == True)

print("Test 5: Empty tree")
print(is_valid_bst(None) == True)
