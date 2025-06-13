class MinHeap:
    def __init__(self):
        """Initializes an empty heap."""
        self.heap = []

    def is_empty(self):
        """Returns True if the heap is empty, otherwise False."""
        return len(self.heap) == 0
    
    
### 3 Test Cases

# Test Case 1
heap = MinHeap()
print(heap.is_empty())  # Expected: True

# Test Case 2
heap = MinHeap()
heap.heap.append(10)  # Simulating insertion
print(heap.is_empty())  # Expected: False

# Test Case 3
heap = MinHeap()
print("Initial state:", heap.heap)  # Expected: []
print("Is heap empty?", heap.is_empty())  # Expected: True

