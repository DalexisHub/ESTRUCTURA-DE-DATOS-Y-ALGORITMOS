# List to store test results
test_results = []
# Helper function to record test results with emoji and boolean value
def record_test(test_name, condition):
    emoji = "✅" if condition else "❌"  # Choose emoji based on result
    # Append formatted result to the list
    test_results.append(f"{emoji} {test_name} -> {condition}")
# Definition of the MinHeap class
class MinHeap:
    # Constructor: initializes the heap as an empty list
    def __init__(self):
        self.heap = []

    # Inserts a new value into the heap
    def insert(self, value):
        self.heap.append(value)                  # Add new value to the end
        self.heapifyup(len(self.heap) - 1)       # Restore the min-heap property

    # Moves the inserted value up until min-heap property is restored
    def heapifyup(self, index):
        parent = self.parentindex(index)         # Get parent index
        while parent >= 0 and self.heap[index] < self.heap[parent]:
            # Swap with parent if smaller
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent                       # Move index up to parent
            parent = self.parentindex(index)     # Update parent index

    # Returns the index of the parent node
    def parentindex(self, index):
        return (index - 1) // 2 if index > 0 else -1

    # Returns the number of elements in the heap
    def size(self):
        return len(self.heap)

    # Returns the minimum value (root of heap) without removing it
    def peek(self):
        return self.heap[0] if self.heap else None

# Function to run all tests defined in Challenge 3
def run_test():
    heap = MinHeap()

    # 1.3.1: Single element insertion
    heap.insert(5)
    record_test("1.3.1 Single element insertion", heap.heap == [5])

    # 1.3.2: Multiple insertions
    heap.insert(3)
    heap.insert(8)
    heap.insert(1)
    record_test("1.3.2 Multiple insertions", len(heap.heap) == 4)

    # 1.3.3: Minimum tracking (root should be smallest)
    record_test("1.3.3 Minimum tracking", heap.peek() == 1)

    # 1.3.4: Heap property validation (every parent must be <= children)
    valid_heap = all(
        (heap.heap[i] <= heap.heap[2 * i + 1] if 2 * i + 1 < len(heap.heap) else True) and
        (heap.heap[i] <= heap.heap[2 * i + 2] if 2 * i + 2 < len(heap.heap) else True)
        for i in range(len(heap.heap) // 2)
    )
    record_test("1.3.4 Heap property validation", valid_heap)

    # 1.3.5: Size consistency (should match number of inserted values)
    record_test("1.3.5 Size consistency", heap.size() == 4)

# 🚀 Run all tests
run_test()

# 📋 Print test summary
for r in test_results:
    print(r)

