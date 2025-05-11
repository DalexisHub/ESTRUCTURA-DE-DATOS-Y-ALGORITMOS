from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          
        self.left = left        
        self.right = right      

class BinaryTree:
    def __init__(self):
        self.root = None        
    
    def build_tree_from_list(self, values):
        """Builds a binary tree from a list of values using level-order traversal"""
        if not values or values[0] is None:
            return             
        
        self.root = TreeNode(values[0])  
        queue = deque([self.root])       
        i = 1                           
        
        while queue and i < len(values):
            node = queue.popleft()      
            if i < len(values):
                if values[i] is not None:
                    node.left = TreeNode(values[i])  
                    queue.append(node.left)          
                i += 1                               
           
            if i < len(values):
                if values[i] is not None:
                    node.right = TreeNode(values[i]) 
                    queue.append(node.right)          
                i += 1                                


def serialize(root):
    """Serializes a binary tree using level-order traversal"""
    if not root:
        return "N"             
    
    result = []                 
    queue = deque([root])       
    
    while queue:
        node = queue.popleft()  
        
        if node:
            result.append(str(node.val))  
            queue.append(node.left)       
            queue.append(node.right)     
        else:
            result.append('N')           
    
    while result and result[-1] == 'N':
        result.pop()
        
    return ','.join(result)     

def deserialize(data):
    """Deserializes a string to a binary tree"""
    if data == "N":
        return None             
    
    values = data.split(',')    
    root = TreeNode(int(values[0]))  
    queue = deque([root])       
    i = 1                       
    
    while queue and i < len(values):
        node = queue.popleft()  
        
      
        if i < len(values):
            left_val = values[i]
            i += 1
            if left_val != 'N':
                node.left = TreeNode(int(left_val))  
                queue.append(node.left)             
        
        if i < len(values):
            right_val = values[i]
            i += 1
            if right_val != 'N':
                node.right = TreeNode(int(right_val))  
                queue.append(node.right)              
    
    return root

def print_tree(root, level=0, prefix="Root: "):
    """Prints a visual representation of the tree"""
    if root is not None:
        print(" " * level + prefix + str(root.val))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")   
            print_tree(root.right, level + 1, "R--- ")  

def are_trees_equal(root1, root2):
    """Verifies if two trees are structurally identical with same values"""
    if not root1 and not root2:
        return True                       
    if not root1 or not root2:
        return False                      
    return (root1.val == root2.val and    
            are_trees_equal(root1.left, root2.left) and   
            are_trees_equal(root1.right, root2.right))    

def test_serialize_deserialize():
    """Tests the serialize and deserialize functions"""
    # Test Case 1: Normal binary tree
    tree1 = BinaryTree()
    tree1.build_tree_from_list([1, 2, 3, 4, 5, None, 6])
    
    # Test Case 2: Left-skewed tree
    tree2 = BinaryTree()
    tree2.build_tree_from_list([1, 2, None, 3, None, None, None, 4])
    
    # Test Case 3: Right-skewed tree
    tree3 = BinaryTree()
    tree3.build_tree_from_list([1, None, 2, None, None, None, 3, None, None, None, None, None, None, None, 4])
    
    cases = [
        (tree1, "Case 1: Normal binary tree 🌳"),
        (tree2, "Case 2: Left-skewed tree 📐⬅️"),
        (tree3, "Case 3: Right-skewed tree 📐➡️")
    ]
    
    for tree, description in cases:
        print(f"\n{description}")
        print("Original tree:")
        print_tree(tree.root)
        
        # Serialize
        serialized = serialize(tree.root)
        print(f"Serialized: {serialized}")
        
        # Deserialize
        deserialized = deserialize(serialized)
        print("Deserialized tree:")
        print_tree(deserialized)
        
        # Verify that trees are identical
        identical = are_trees_equal(tree.root, deserialized)
        print(f"Verification: {'✅ PASSED' if identical else '❌ FAILED'}")
        
        print("-" * 50)

# Run tests
if __name__ == "__main__":
    test_serialize_deserialize()