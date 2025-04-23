class CircularQueue:
    """Implementation of a circular queue using a fixed-size list."""

    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, value):
        if self.is_full():
            raise Exception("Queue is full")
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        value = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return value

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.size

    def show(self):
        """Return the current contents of the queue."""
        result = []
        index = self.front
        for _ in range(self.count):
            result.append(self.queue[index])
            index = (index + 1) % self.size
        return result


def rotate_array(nums, k):
    """Rotate the array to the right by k steps using a circular queue."""
    if not nums or k <= 0:
        return nums

    n = len(nums)
    k = k % n  # Handle case where k > n

    queue = CircularQueue(n)

    # Step 1: Enqueue all elements
    for num in nums:
        queue.enqueue(num)

    # Step 2: Rotate - move the first n-k elements to the rear
    for _ in range(n - k):
        queue.enqueue(queue.dequeue())

    # Step 3: Show final rotated queue
    return queue.show()


# --- Test cases ---

print("code execution:", rotate_array([1, 2, 3, 4, 5, 6, 7], 3))    
# Output: [5, 6, 7, 1, 2, 3, 4]
print("Test Case 1:", rotate_array([10, 20, 30, 40, 50], 2))     
# Output: [40, 50, 10, 20, 30]
print("Test Case 2:", rotate_array([100, 200, 300], 4))          
# Output: [300, 100, 200]
print("Test Case 3:", rotate_array([9, 8, 7, 6, 5], 1))          
# Output: [5, 9, 8, 7, 6]
