class AVLNode:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

def get_height(node):
    return node.height if node else 0

def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0

def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def get_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def delete(root, key):
    # Step 1: Standard BST deletion
    if not root:
        return root
    elif key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        temp = get_min_value_node(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)

    # Step 2: Update height
    root.height = 1 + max(get_height(root.left), get_height(root.right))

    # Step 3: Get balance factor
    balance = get_balance(root)

    # Step 4: Rebalance cases
    # LL
    if balance > 1 and get_balance(root.left) >= 0:
        return right_rotate(root)
    # LR
    if balance > 1 and get_balance(root.left) < 0:
        root.left = left_rotate(root.left)
        return right_rotate(root)
    # RR
    if balance < -1 and get_balance(root.right) <= 0:
        return left_rotate(root)
    # RL
    if balance < -1 and get_balance(root.right) > 0:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root

def pre_order(node):
    if not node:
        return []
    return [node.key] + pre_order(node.left) + pre_order(node.right)

# Case 1: Simple deletion with no rebalancing
root = AVLNode(10)
root.left = AVLNode(5)
root.right = AVLNode(15)
root = delete(root, 5)
print("Test 1:", pre_order(root))  # ➞ [10, 15]

# Case 2: Deletion causing LL rotation
root = AVLNode(30)
root.left = AVLNode(20)
root.left.left = AVLNode(10)
root = delete(root, 30)
print("Test 2:", pre_order(root))  # ➞ [20, 10]

# Case 3: Deletion causing RL rotation
root = AVLNode(10)
root.right = AVLNode(30)
root.right.left = AVLNode(20)
root = delete(root, 10)
print("Test 3:", pre_order(root))  # ➞ [20, 30]
