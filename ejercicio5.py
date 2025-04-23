from collections import deque

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.buffer = deque(maxlen=size)

    def add(self, value):
        self.buffer.append(value)

    def get_latest(self):
        return list(self.buffer)

    def get_statistics(self):
        if not self.buffer:
            return {"mean": None, "min": None, "max": None}
        values = list(self.buffer)
        return {
            "mean": sum(values) / len(values),
            "min": min(values),
            "max": max(values)
        }

cb = CircularBuffer(3)
cb.add(5)
cb.add(10)
cb.add(15)
print(cb.get_latest())      # [5, 10, 15]
cb.add(20)
print(cb.get_latest())      # [10, 15, 20]
print(cb.get_statistics())  # {'mean': 15.0, 'min': 10, 'max': 20}

cb = CircularBuffer(4)
cb.add(1)
cb.add(2)
print(cb.get_latest())  # [1, 2]

cb = CircularBuffer(2)
cb.add(1)
cb.add(2)
cb.add(3)
print(cb.get_latest())  # [2, 3]

cb = CircularBuffer(3)
cb.add(2)
cb.add(4)
cb.add(6)
print(cb.get_statistics())  # {'mean': 4.0, 'min': 2, 'max': 6}
