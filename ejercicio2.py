class MyCircularDeque:
    
    def __init__(self, k: int):
        self.size = k
        self.deque = [None] * k
        self.front = -1
        self.rear = -1

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.front = (self.front - 1 + self.size) % self.size
        self.deque[self.front] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.deque[self.rear] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:  # Solo un elemento
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:  # Solo un elemento
            self.front = self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.size) % self.size
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque[self.rear]

deque = MyCircularDeque(3)
print(deque.insertLast(1))    # True
print(deque.insertLast(2))    # True
print(deque.insertFront(3))   # True
print(deque.insertFront(4))   # False, está llena
print(deque.getRear())        # 2
print(deque.isFull())         # True
print(deque.deleteLast())     # True
print(deque.insertFront(4))   # True
print(deque.getFront())       # 4
