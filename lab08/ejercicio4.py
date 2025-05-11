# Node Definition
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BinaryTree Definition
class BinaryTree:
    def __init__(self):
        self.root = None

    # Method to build the tree from a list
    def build_tree_from_list(self, lst):
        if not lst:
            return None
        
        self.root = self._build_tree(lst, 0)

    def _build_tree(self, lst, index):
        if index >= len(lst) or lst[index] is None:
            return None
        node = Node(lst[index])
        node.left = self._build_tree(lst, 2 * index + 1)
        node.right = self._build_tree(lst, 2 * index + 2)
        return node

    # Method to perform vertical traversal
    def vertical_order_traversal(self):
        if not self.root:
            return []

        column_dict = {}

        # DFS function to assign horizontal distance
        def dfs(node, distance):
            if node is None:
                return

            if distance not in column_dict:
                column_dict[distance] = []
            column_dict[distance].append(node.value)

            # Traverse child nodes
            dfs(node.left, distance - 1)
            dfs(node.right, distance + 1)

        # Perform DFS from root with distance 0
        dfs(self.root, 0)

        # Sort by horizontal distances
        sorted_columns = sorted(column_dict.keys())

        result = []
        for col in sorted_columns:
            result.append(column_dict[col])

        return result

# Test cases
def test_vertical_order_traversal():
    """Test the vertical_order_traversal function. 📏"""
    # Test Case 1: Normal binary tree 🌳
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4   5   6
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    result1 = tree1.vertical_order_traversal()
    print("Test Case 1 - Expected Output: [[4], [2], [1, 5], [3], [6]]")
    print("Test Case 1 - Actual Output:", result1)
    assert result1 == [[4], [2], [1, 5], [3], [6]]
    # Test Case 2: Vertical line tree 📏
    #      1
    #     /
    #    2
    #   /
    #  3
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3])
    result2 = tree2.vertical_order_traversal()
    print("Test Case 2 - Expected Output: [[3], [2], [1]]")
    print("Test Case 2 - Actual Output:", result2)
    assert result2 == [[3], [2], [1]]
    # Test Case 3: Single node tree 🌱
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1])
    result3 = tree3.vertical_order_traversal()
    print("Test Case 3 - Expected Output: [[1]]")
    print("Test Case 3 - Actual Output:", result3)
    assert result3 == [[1]]
# Run the tests
test_vertical_order_traversal()
