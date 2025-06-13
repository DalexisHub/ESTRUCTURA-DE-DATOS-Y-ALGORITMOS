class MinHeap:
    def __init__(self):
        self.heap = []

    def delete_min(self):
        if not self.heap:
            print("Heap is empty. Returning None.")
            return None

        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        min_val = self.heap.pop()

        if self.heap:
            self._heapify_down(0)

        print(f"Deleted min: {min_val}")
        print(f"Heap after delete_min: {self.heap}")
        return min_val

    def _heapify_down(self, index):
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
        print(f"Inserted {val}. Heap is now: {self.heap}")

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[index] < self.heap[parent]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self._heapify_up(parent)

    def __repr__(self):
        return f"MinHeap({self.heap})"

# Prueba 1: Heap vacío
print("Test 1: Delete from empty heap")
heap = MinHeap()
heap.delete_min()

# Prueba 2: Un solo elemento
print("\nTest 2: Delete from heap with one element")
heap.insert(10)
heap.delete_min()

# Prueba 3: Múltiples elementos
print("\nTest 3: Delete from heap with multiple elements")
for val in [5, 3, 8, 1, 2]:
    heap.insert(val)
heap.delete_min()  # Should delete 1

# Prueba 4: Eliminaciones secuenciales
print("\nTest 4: Sequential deletes")
heap = MinHeap()
for val in [4, 7, 6, 2, 9]:
    heap.insert(val)
while heap.heap:
    heap.delete_min()

# Prueba 5: Árbol más complejo
print("\nTest 5: Complex tree structure")
heap = MinHeap()
for val in [15, 10, 20, 17, 8, 25, 5]:
    heap.insert(val)
heap.delete_min()  # Should delete 5
