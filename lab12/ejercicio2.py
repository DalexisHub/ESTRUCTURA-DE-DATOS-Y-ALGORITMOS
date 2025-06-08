class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def rotate_right(self, z):
        y = z.left
        T2 = y.right
        y.right = z
        z.left = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)
        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

def test_rotations():
    tree = AVLTree()

    z = AVLNode(10)
    z.right = AVLNode(20)
    z.right.right = AVLNode(30)
    tree.update_height(z.right.right)
    tree.update_height(z.right)
    tree.update_height(z)
    z = tree.rotate_left(z)
    test1_result = z.key == 20
    print(f"🧪 Test 1 Result: {test1_result} ✅" if test1_result else f"🧪 Test 1 Result: {test1_result} ❌")

    z = AVLNode(30)
    z.left = AVLNode(20)
    z.left.left = AVLNode(10)
    tree.update_height(z.left.left)
    tree.update_height(z.left)
    tree.update_height(z)
    z = tree.rotate_right(z)
    test2_result = z.key == 20
    print(f"🧪 Test 2 Result: {test2_result} ✅" if test2_result else f"🧪 Test 2 Result: {test2_result} ❌")

    test3_result = (z.height == 2 and 
                   tree.get_height(z.left) == 1 and 
                   tree.get_height(z.right) == 1)
    print(f"🧪 Test 3 Result: {test3_result} ✅" if test3_result else f"🧪 Test 3 Result: {test3_result} ❌")

    test4_result = (z.left.key == 10 and z.right.key == 30 and
                   z.left.left is None and z.left.right is None and
                   z.right.left is None and z.right.right is None)
    print(f"🧪 Test 4 Result: {test4_result} ✅" if test4_result else f"🧪 Test 4 Result: {test4_result} ❌")

    tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = tree.insert(root, key)

    def is_balanced(node):
        if not node:
            return True
        balance = tree.get_balance(node)
        return (abs(balance) <= 1 and 
                is_balanced(node.left) and 
                is_balanced(node.right))

    test5_result = is_balanced(root)
    print(f"🧪 Test 5 Result: {test5_result} ✅" if test5_result else f"🧪 Test 5 Result: {test5_result} ❌")

if __name__ == "__main__":
    test_rotations()
