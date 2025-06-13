class MaxHeap:
    # Constructor initializes an empty heap list
    def __init__(self):
        self.heap = []

    def insert(self, value):
        # Add the new value to the end of the heap
        self.heap.append(value)

        # Restore the max-heap property by moving the new value up
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        # Continue until reaching the root node
        while index > 0:
            # Get the index of the parent node
            parent = (index - 1) // 2

            # If current node is greater than parent, swap
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent  # Move up to the parent's index
            else:
                break  # Stop if heap property is satisfied

    def delete_max(self):
        # If the heap is empty, return None
        if not self.heap:
            return None

        # Save the max value (root of the heap)
        max_val = self.heap[0]

        # Move the last element to the root and remove the last element
        self.heap[0] = self.heap[-1]
        self.heap.pop()

        # Restore the max-heap property
        self._heapify_down(0)

        return max_val

    def _heapify_down(self, index):
        # Length of the heap
        size = len(self.heap)

        # Loop while the node has at least one child
        while 2 * index + 1 < size:
            # Get indices of left and right children
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            # Find the largest among current, left, and right
            if left < size and self.heap[left] > self.heap[largest]:
                largest = left
            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            # If the largest is not the current node, swap and continue
            if largest != index:
                self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
                index = largest
            else:
                break  # Stop if heap property is satisfied

# 🧪 Test cases
def test_max_heap():
    h = MaxHeap()
    h.insert(1); print("🦁 Test 1:", h.heap == [1])
    for v in [3, 2, 8, 5]:
        h.insert(v)
    print("🦁 Test 2:", h.heap[0] == max(h.heap))
    h.delete_max(); print("🦁 Test 3:", h.heap[0] == max(h.heap))
    h = MaxHeap()
    for v in [5, 3, 1]:
        h.insert(v)
    h.delete_max(); print("🦁 Test 4:", h.heap == [3, 1])
    h = MaxHeap(); h.insert(10)
    print("🦁 Test 5:", h.delete_max() == 10 and h.heap == [])

test_max_heap()
