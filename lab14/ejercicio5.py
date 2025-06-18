test_results = []

# Utility function to record test outcomes
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"
    test_results.append(f"{emoji} {test_name}")

class MaxHeap:
    def __init__(self):
        # Initialize the heap as an empty list
        self.heap = []

    def insert(self, value):
        # Add the value to the end of the heap
        self.heap.append(value)
        # Restore max-heap property by moving the new element up
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        # If heap is empty, return None
        if not self.heap:
            return None
        # Swap the max element (root) with the last element
        self._swap(0, len(self.heap) - 1)
        # Remove and store the max value
        max_value = self.heap.pop()
        # Restore max-heap property from the root down
        self._heapify_down(0)
        # Return the maximum value that was removed
        return max_value

    def build_heap(self, array):
        # Replace current heap with the new array
        self.heap = array[:]
        # Start from the last non-leaf node and heapify down each node
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_up(self, index):
        # Continue bubbling up until root or max-heap property is restored
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] > self.heap[parent]:
            self._swap(index, parent)
            index = parent
            parent = (index - 1) // 2

    def _heapify_down(self, index):
        # Move down the node at index to restore max-heap property
        size = len(self.heap)
        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            # Check if left child is larger than current largest
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            # Check if right child is larger than current largest
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            # If current node is larger than both children, stop
            if largest == index:
                break

            # Otherwise, swap and continue down
            self._swap(index, largest)
            index = largest

    def _swap(self, i, j):
        # Swap two elements in the heap
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

# Test function for verifying heap behavior
def test_1_5():
    heap = MaxHeap()
    
    # 1.5.1 MaxHeap insertion test
    heap.insert(3)  # Insert 3
    heap.insert(1)  # Insert 1
    heap.insert(5)  # Insert 5, should become the root
    record_test("1.5.1 MaxHeap insertion", heap.heap[0] == 5)

    # 1.5.2 MaxHeap deletion test
    max_val = heap.delete_max()  # Should return 5 and remove it
    record_test("1.5.2 MaxHeap deletion", max_val == 5)

    # 1.5.3 Build heap from unordered array
    heap.build_heap([3, 1, 4, 1, 5, 9, 2])
    record_test("1.5.3 Build heap from array", heap.heap[0] == max(heap.heap))

    # 1.5.4 Validate max-heap property for all internal nodes
    valid_max_heap = all(
        heap.heap[i] >= heap.heap[2*i+1] if 2*i+1 < len(heap.heap) else True
        and heap.heap[i] >= heap.heap[2*i+2] if 2*i+2 < len(heap.heap) else True
        for i in range(len(heap.heap)//2)
    )
    record_test("1.5.4 Heap property verification", valid_max_heap)

    # 1.5.5 Ensure build_heap handles empty arrays without crashing
    heap.build_heap([])
    record_test("1.5.5 Empty array handling", len(heap.heap) == 0)

# 🚀 Run the tests
test_1_5()

# 📋 Print all test results
for r in test_results:
    print(r)
