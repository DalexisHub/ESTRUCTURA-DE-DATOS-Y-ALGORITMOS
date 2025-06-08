class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2
        self.update_height(z)
        self.update_height(y)
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        self.update_height(root)
        balance = self.get_balance(root)

        # Left heavy
        if balance > 1:
            if key < root.left.key:  # Left-Left
                return self.rotate_right(root)
            else:  # Left-Right
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        # Right heavy
        if balance < -1:
            if key > root.right.key:  # Right-Right
                return self.rotate_left(root)
            else:  # Right-Left
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def is_avl_balanced(self, root):
        def check(node):
            if not node:
                return 0  # An empty tree is balanced

            left_height = check(node.left)
            if left_height == -1:
                return -1

            right_height = check(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1

            return 1 + max(left_height, right_height)

        return check(root) != -1

# 🧪 Test Cases
def test_is_avl_balanced():
    avl = AVLTree()

    # Test 1: Automatically balanced tree
    root = None
    for val in [20, 10, 30]:
        root = avl.insert(root, val)
    print("🧪 Test 1:", avl.is_avl_balanced(root) == True)  # ✅

    # Test 2: Manually unbalanced tree (no rebalancing)
    unbalanced = AVLNode(10)
    unbalanced.right = AVLNode(20)
    unbalanced.right.right = AVLNode(30)
    print("🧪 Test 2:", avl.is_avl_balanced(unbalanced) == False)  # ❌

    # Test 3: Empty tree
    print("🧪 Test 3:", avl.is_avl_balanced(None) == True)  # 🌱

    # Test 4: Deep imbalance
    deep_unbalanced = AVLNode(50)
    deep_unbalanced.left = AVLNode(30)
    deep_unbalanced.left.left = AVLNode(20)
    deep_unbalanced.left.left.left = AVLNode(10)
    print("🧪 Test 4:", avl.is_avl_balanced(deep_unbalanced) == False)  # ⚠️

    # Test 5: Larger balanced tree
    root2 = None
    for val in [40, 20, 60, 10, 30, 50, 70]:
        root2 = avl.insert(root2, val)
    print("🧪 Test 5:", avl.is_avl_balanced(root2) == True)  # ✅

# 🚀 Run tests
test_is_avl_balanced()
