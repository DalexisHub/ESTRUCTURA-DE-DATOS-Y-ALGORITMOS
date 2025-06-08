class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Height of node initialized to 1 for leaf node


class AVLTree:
    def insert(self, root, key):
        # PASO 1: Perform normal BST insertion
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # PASO 2: Update height of the ancestor node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # PASO 3: Get balance factor
        balance = self.get_balance(root)

        # PASO 4: Check and apply rotations if unbalanced

        # LL
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)

        # RR 
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)

        # LR
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # RL
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def pre_order(self, root):
        if not root:
            return []
        return [root.key] + self.pre_order(root.left) + self.pre_order(root.right)

def run_tests():
    avl = AVLTree()
    root = None

    values = [10, 20, 30, 40, 50, 25]  # Triggers case1, case2, case3, case4 
    for val in values:
        root = avl.insert(root, val)

    print("Pre-order Traversal After Insertions:")
    print(avl.pre_order(root))  # Expected balanced AVL output

run_tests()