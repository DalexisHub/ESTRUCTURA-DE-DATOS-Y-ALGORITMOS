class MinHeap:
    def __init__(self):
        # Constructor initializes an empty list to represent the heap
        self.heap = []

    def is_empty(self):
        # Returns True if heap contains no elements; False otherwise
        return len(self.heap) == 0

    def size(self):
        # Returns the number of elements currently in the heap
        return len(self.heap)

    def peek(self):
        # If the heap is empty, return None (to avoid IndexError)
        if self.is_empty():
            return None
        # Return the first element, which is the minimum in a min-heap
        return self.heap[0]

def run_tests():
    print("Running Tests for MinHeap Foundation...\n")
    
    # 1.1.1: Empty heap initialization
    h = MinHeap()
    assert h.is_empty() == True, "Test 1.1.1 Failed: Heap should be empty"
    
    # 1.1.2: Size tracking
    h.heap.extend([1, 3, 5])  # Simulate adding elements directly
    assert h.size() == 3, "Test 1.1.2 Failed: Size should be 3"
    
    # 1.1.3: Peek functionality
    assert h.peek() == 1, "Test 1.1.3 Failed: Peek should return 1"
    
    # 1.1.4: Empty heap edge case
    h2 = MinHeap()
    assert h2.peek() is None, "Test 1.1.4 Failed: Peek on empty heap should return None"
    
    # 1.1.5: Type validation
    assert isinstance(h.is_empty(), bool), "Test 1.1.5 Failed: is_empty() should return bool"
    assert isinstance(h.size(), int), "Test 1.1.5 Failed: size() should return int"
    assert isinstance(h.peek(), (int, type(None))), "Test 1.1.5 Failed: peek() should return int or None"
    
    print("✅ All tests passed for Challenge 1.\n")

run_tests()
