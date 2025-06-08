from collections import deque

# 🌳 AVL Node definition
class Node:
    def __init__(self, value):
        self.value = value  # Node value
        self.left = None    # Left child
        self.right = None   # Right child
        self.height = 1     # Node height (starts at 1 for leaf)

# 🔧 AVL Tree class
class AVLTree:
    # 📏 Get the height of a node
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # ♻️ Update height based on children
    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    # ↩️ Right rotation for balancing
    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        self.update_height(z)
        self.update_height(y)

        return y

    # ↪️ Left rotation for balancing
    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        self.update_height(z)
        self.update_height(y)

        return y

    # ⚖️ Get balance factor
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ➕ Insert a value into the AVL tree
    def insert(self, node, value):
        if not node:
            return Node(value)
        
        # Traverse to correct position
        if value < node.value:
            node.left = self.insert(node.left, value)
        else:
            node.right = self.insert(node.right, value)

        # Update height
        self.update_height(node)

        # Get balance factor
        balance = self.get_balance(node)

        # Perform rotations if unbalanced
        # Left Left
        if balance > 1 and value < node.left.value:
            return self.rotate_right(node)
        # Right Right
        if balance < -1 and value > node.right.value:
            return self.rotate_left(node)
        # Left Right
        if balance > 1 and value > node.left.value:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        # Right Left
        if balance < -1 and value < node.right.value:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # 📡 Level-order print with heights
    def print_level_order(self, root):
        if not root:
            return
        
        queue = deque([root])  # Queue for BFS
        while queue:
            level_size = len(queue)
            level_nodes = []

            for _ in range(level_size):
                node = queue.popleft()
                # Save value and height
                level_nodes.append(f"{node.value}(h{node.height})")

                # Add children to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Print the current level
            print(", ".join(level_nodes))
def test_level_order_heights():
    avl = AVLTree()

    print("🧪 Test 1: [10, 5, 15]")
    root = None
    for val in [10, 5, 15]:
        root = avl.insert(root, val)
    avl.print_level_order(root)
    print("Expected:\n10(h2)\n5(h1), 15(h1)\n")

    print("🧪 Test 2: [10, 5, 15, 2, 7]")
    root = None
    for val in [10, 5, 15, 2, 7]:
        root = avl.insert(root, val)
    avl.print_level_order(root)
    print("Expected:\n10(h3)\n5(h2), 15(h1)\n2(h1), 7(h1)\n")

    print("🧪 Test 3: Empty Tree")
    avl.print_level_order(None)
    print("Expected: (nothing)\n")

    print("🧪 Test 4: Unbalanced Input [30, 20, 10] (requires rotation)")
    root = None
    for val in [30, 20, 10]:  # Causes left-left imbalance
        root = avl.insert(root, val)
    avl.print_level_order(root)
    print("Expected:\n20(h2)\n10(h1), 30(h1)\n")

    print("🧪 Test 5: Large Tree [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35]")
    root = None
    for val in [40, 20, 60, 10, 30, 50, 70, 5, 15, 25, 35]:
        root = avl.insert(root, val)
    avl.print_level_order(root)
    print("Expected: Multiple levels with accurate heights.\n")

# 🚀 Run tests
test_level_order_heights()