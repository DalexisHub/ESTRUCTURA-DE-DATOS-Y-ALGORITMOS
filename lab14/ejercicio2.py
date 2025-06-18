class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent_index(self, index):
        if index <= 0 or index >= len(self.heap):
            return None
        return (index - 1) // 2

    def _left_child_index(self, index):
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    def _right_child_index(self, index):
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    def _has_left_child(self, index):
        return self._left_child_index(index) is not None

    def _has_right_child(self, index):
        return self._right_child_index(index) is not None


#Test and print results
h = MinHeap()
h.heap = [10, 20, 30, 40, 50]  # Indices: 0   1   2   3   4

print("1.2.1: Parent of index 4:", h._parent_index(4))  # Expected: 1
print("1.2.2: Left child of index 1:", h._left_child_index(1))  # Expected: 3
print("1.2.2: Right child of index 1:", h._right_child_index(1))  # Expected: 4
print("1.2.3: Parent of root index 0:", h._parent_index(0))  # Expected: None

print("1.2.4: Has left child (index 1):", h._has_left_child(1))  # Expected: True
print("1.2.4: Has right child (index 1):", h._has_right_child(1))  # Expected: True
print("1.2.4: Has left child (index 2):", h._has_left_child(2))  # Expected: False
print("1.2.4: Has right child (index 2):", h._has_right_child(2))  # Expected: False

print("1.2.5: Parent of invalid index 10:", h._parent_index(10))  # Expected: None
print("1.2.5: Left child of invalid index 10:", h._left_child_index(10))  # Expected: None
print("1.2.5: Right child of invalid index 10:", h._right_child_index(10))  # Expected: None
print("1.2.5: Has left child (index 10):", h._has_left_child(10))  # Expected: False
print("1.2.5: Has right child (index 10):", h._has_right_child(10))  # Expected: False
