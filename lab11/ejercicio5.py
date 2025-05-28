class Node:
    def __init__(self, value):
        self.value = value
        self.left = None  # Will act as previous in the doubly linked list
        self.right = None  # Will act as next in the doubly linked list

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Insert value into BST"""
        if not self.root:
            self.root = Node(value)
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(value)
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(value)
                    return

    def build_from_list(self, values):
        """Build BST from a list of values"""
        for v in values:
            self.insert(v)

class BinarySearchTree(BinarySearchTree):
    def bst_to_dll(self):
        """🔁 Convert BST to sorted circular doubly linked list"""

        if not self.root:
            return None  # Empty tree case

        # Initialize pointers for tracking the head and previous node
        self.first = None  # First node in the DLL (smallest element)
        self.last = None   # Last visited node during traversal

        def inorder(node):
            """Recursive inorder traversal to link nodes"""
            if not node:
                return

            # Traverse left subtree
            inorder(node.left)

            # Link current node with the previous node (self.last)
            if self.last:
                self.last.right = node   # last ➡️ current
                node.left = self.last    # current ⬅️ last
            else:
                self.first = node  # This is the first (smallest) node

            self.last = node  # Update last to current

            # Traverse right subtree
            inorder(node.right)

        # Start inorder traversal from root
        inorder(self.root)

        # Connect head and tail to make it circular ⭕
        self.first.left = self.last
        self.last.right = self.first

        return self.first  # Return head of circular doubly linked list


def validate_circular_dll(head, expected_values):
    if not head:
        return expected_values == []
    values = []
    current = head
    while True:
        values.append(current.value)
        current = current.right
        if current == head:
            break
    return values == expected_values

def test_bst_to_dll():
    bst1 = BinarySearchTree()
    bst1.build_from_list([2, 1, 3])
    head1 = bst1.bst_to_dll()
    print("🧪 Test 1:", validate_circular_dll(head1, [1, 2, 3]) == True)

    bst2 = BinarySearchTree()
    bst2.build_from_list([4, 2, 6, 1, 3, 5, 7])
    head2 = bst2.bst_to_dll()
    print("🧪 Test 2:", validate_circular_dll(head2, [1, 2, 3, 4, 5, 6, 7]) == True)

    bst3 = BinarySearchTree()
    bst3.build_from_list([5])
    head3 = bst3.bst_to_dll()
    print("🧪 Test 3:", validate_circular_dll(head3, [5]) == True)

    bst4 = BinarySearchTree()
    bst4.build_from_list([1, 2, 3, 4])
    head4 = bst4.bst_to_dll()
    print("🧪 Test 4:", validate_circular_dll(head4, [1, 2, 3, 4]) == True)

    bst5 = BinarySearchTree()
    head5 = bst5.bst_to_dll()
    print("🧪 Test 5:", head5 is None)

test_bst_to_dll()
