class QueueWithStacks:

    def __init__(self):
        self.stack_in = []   # Pila para encolar
        self.stack_out = []  # Pila para desencolar

    def enqueue(self, value):
        """Agrega un elemento al final de la cola."""
        self.stack_in.append(value)

    def dequeue(self):
        """Elimina y retorna el elemento al frente de la cola."""
        if self.isEmpty():
            raise IndexError("Error: La cola está vacía. No se puede eliminar.")
        self._transfer_if_needed()
        return self.stack_out.pop()

    def peek(self):
        """Retorna el elemento al frente sin eliminarlo."""
        if self.isEmpty():
            raise IndexError("Error: La cola está vacía. No hay frente.")
        self._transfer_if_needed()
        return self.stack_out[-1]

    def isEmpty(self):
        """Retorna True si la cola está vacía."""
        return not self.stack_in and not self.stack_out

    def _transfer_if_needed(self):
        """Transfiere elementos de stack_in a stack_out si este último está vacío."""
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

def run_tests():
    print("=== Pruebas para QueueWithStacks ===")
    
    queue = QueueWithStacks()
    
    assert queue.isEmpty() == True
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    assert queue.peek() == 10
    assert queue.dequeue() == 10
    assert queue.peek() == 20
    assert queue.dequeue() == 20
    assert queue.dequeue() == 30
    try:
        queue.dequeue()
    except IndexError as e:
        print("Excepción atrapada correctamente:", e)
    
    assert queue.isEmpty() == True
    print("Todas las pruebas pasaron correctamente.")

run_tests()
