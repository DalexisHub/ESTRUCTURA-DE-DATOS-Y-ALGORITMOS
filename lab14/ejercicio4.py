# ✅ Title: Min-Heap Deletion with Downward Percolation (Heapify Down)
# Test result collector
test_results = []
# Function to record test outcomes with emoji and boolean condition
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name} -> {condition}")
# MinHeap class that supports deletion while preserving the heap structure
class MinHeap:
    def __init__(self):
        self.heap = []  # Initialize an empty heap

    # Deletes and returns the smallest element (the root)
    def delete_min(self):
        if not self.heap:
            return None  # Case 1.4.1: Empty heap, return None
        if len(self.heap) == 1:
            return self.heap.pop()  # Case 1.4.2: Single element, remove and return it
        min_value = self.heap[0]  # Store the root value
        self.heap[0] = self.heap.pop()  # Move last element to the root
        self._heapify_down(0)  # Restore heap order by percolating down
        return min_value  # Return the original minimum

    # Restores heap property by moving element down to correct position
    def _heapify_down(self, index):
        while self._has_left_child(index):  # Continue if left child exists
            smaller_child_index = self._left_child_index(index)
            if self._has_right_child(index) and self.heap[self._right_child_index(index)] < self.heap[smaller_child_index]:
                smaller_child_index = self._right_child_index(index)
            if self.heap[index] <= self.heap[smaller_child_index]:
                break  # Heap property satisfied, stop
            # Swap current element with smaller child
            self.heap[index], self.heap[smaller_child_index] = self.heap[smaller_child_index], self.heap[index]
            index = smaller_child_index  # Move index to child and repeat

    # Returns index of left child
    def _left_child_index(self, index):
        return 2 * index + 1

    # Returns index of right child
    def _right_child_index(self, index):
        return 2 * index + 2

    # Checks if left child exists
    def _has_left_child(self, index):
        return self._left_child_index(index) < len(self.heap)

    # Checks if right child exists
    def _has_right_child(self, index):
        return self._right_child_index(index) < len(self.heap)

    # Returns current number of elements in heap
    def size(self):
        return len(self.heap)

# Test function to validate behavior of delete_min and heap property
def test_1_4():
    heap = MinHeap()
    # 1.4.1: Deletion from empty heap
    result = heap.delete_min()
    record_test("1.4.1 Empty heap deletion", result is None)
    # 1.4.2: Deletion from single-element heap
    heap.heap = [5]
    result = heap.delete_min()
    record_test("1.4.2 Single element deletion", result == 5 and heap.size() == 0)
    # 1.4.3: Multiple deletions should return correct values
    heap.heap = [1, 3, 2, 7, 4]
    first = heap.delete_min()
    second = heap.delete_min()
    record_test("1.4.3 Multiple deletions", first == 1 and second == 2)
    # 1.4.4: Check heap property after deletion
    heap.heap = [1, 3, 2, 7, 4, 5]
    heap.delete_min()
    valid_heap = all(
        (heap.heap[i] <= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True) and
        (heap.heap[i] <= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True)
        for i in range(len(heap.heap)//2)
    )
    record_test("1.4.4 Heap property maintenance", valid_heap)
    # 1.4.5: Check size reduction
    initial_size = heap.size()
    heap.delete_min()
    record_test("1.4.5 Size tracking", heap.size() == initial_size - 1)

# 🚀 Run the test suite
test_1_4()

# 📋 Print test results
for r in test_results:
    print(r)
