class PriorityQueue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item, priority):
        self.items.append((item, priority))

    def dequeue(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")

        max_index = 0
        for i in range(1, len(self.items)):
            if self.items[i][1] > self.items[max_index][1]:
                max_index = i

        return self.items.pop(max_index)[0]
    def peek(self):
        if self.is_empty():
            raise IndexError("La cola está vacía")

        max_index = 0
        for i in range(1, len(self.items)):
            if self.items[i][1] > self.items[max_index][1]:
                max_index = i

        return self.items[max_index][0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return f"PriorityQueue: {self.items}"
    
#CASOS DE PRUEBA AQUI:
def pruebas():
    pq = PriorityQueue()

    assert pq.is_empty() == True
    assert pq.size() == 0

    pq.enqueue("Tarea baja", 1)
    pq.enqueue("Tarea crítica", 10)
    pq.enqueue("Tarea media", 5)
    pq.enqueue("Otra tarea media", 5)

    assert pq.peek() == "Tarea crítica"
    assert pq.dequeue() == "Tarea crítica"
    assert pq.dequeue() == "Tarea media"
    assert pq.dequeue() == "Otra tarea media"
    assert pq.dequeue() == "Tarea baja"

    try:
        pq.dequeue()
    except IndexError as e:
        print(f"Error esperado: {e}")

    print("Todas las pruebas pasaron.")

pruebas()