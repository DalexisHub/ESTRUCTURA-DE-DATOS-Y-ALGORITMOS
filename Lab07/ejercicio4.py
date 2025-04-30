from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root):
    """
    Performs a level order traversal of a binary tree.
    
    Args:
        root: The root node of the binary tree
        
    Returns:
        A list containing the values of the nodes in level order traversal
    """
    # If the tree is empty, return an empty list
    if not root:
        return []
    
    # Initialize the queue with the root node
    queue = deque([root])
    # List to store the result
    result = []
    
    # While the queue is not empty
    while queue:
        # Remove the first node from the queue
        current_node = queue.popleft()
        
        # Add the value of the current node to the result
        result.append(current_node.val)
        
        # If the node has a left child, add it to the queue
        if current_node.left:
            queue.append(current_node.left)
        
        # If the node has a right child, add it to the queue
        if current_node.right:
            queue.append(current_node.right)
    
    return result

def test_level_order_traversal():
    # Test Case 1: Normal tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    assert level_order_traversal(root) == [1, 2, 3, 4, 5, 6]
    print("Test Case 1 passed successfully")
    
    # Test Case 2: Empty tree
    empty_tree = None
    assert level_order_traversal(empty_tree) == []
    print("Test Case 2 passed successfully")
    
    # Test Case 3: Single node tree
    single_node = TreeNode(1)
    assert level_order_traversal(single_node) == [1]
    print("Test Case 3 passed successfully")
    
    # Test Case 4: Left-skewed tree
    left_skewed = TreeNode(1)
    left_skewed.left = TreeNode(2)
    left_skewed.left.left = TreeNode(3)
    left_skewed.left.left.left = TreeNode(4)
    assert level_order_traversal(left_skewed) == [1, 2, 3, 4]
    print("Test Case 4 passed successfully")
    print("All tests passed successfully!")

# Run the tests
if __name__ == "__main__":
    test_level_order_traversal()

