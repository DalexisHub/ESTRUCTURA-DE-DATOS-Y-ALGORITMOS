class MinHeap:
    def build_heap(self, array):
        # Copy the given array into the heap
        self.heap = array.copy()

        # Start from the last non-leaf node and heapify down each node
        # This ensures we convert the array into a valid min-heap in O(n) time
        for i in range(len(self.heap) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, index):
        # Get the index of the left and right child
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        # Check if left child exists and is smaller than the current smallest
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        # Check if right child exists and is smaller than the current smallest
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        # If the smallest is not the current index, swap and continue heapifying
        if smallest != index:
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self._heapify_down(smallest)

# 🧪 Test cases
def test_build_heap():
    h = MinHeap()
    h.build_heap([5, 3, 8, 1, 2]); print("🔨 Test 1:", h.heap[0] == 1)
    h.build_heap([7, 6, 5, 4, 3, 2, 1]); print("🔨 Test 2:", h.heap[0] == 1)
    h.build_heap([2, 1]); print("🔨 Test 3:", h.heap == [1, 2])
    h.build_heap([10]); print("🔨 Test 4:", h.heap == [10])
    h.build_heap([]); print("🔨 Test 5:", h.heap == [])

test_build_heap()
