class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía")
            return -1
        dequeued_node = self.front
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.count -= 1
        return dequeued_node.data

    def peek(self):
        if self.is_empty():
            print("La cola está vacía")
            return -1
        return self.front.data
    
    def size(self):
        return self.count
    
# Ejemplo de uso
Cola = Queue()
# Agregar elementos a la cola
Cola.enqueue("Perros")
Cola.enqueue("Gatos")
Cola.enqueue("Tortugas")
# Eliminar y ver elementos de la cola
print(Cola.dequeue())  # Output: "Perros"

# Ver el elemento al frente de la cola
print(Cola.peek())    # Output: "Gatos"

# Verificar el tamaño de la cola y si está vacía
print(Cola.size())    # Output: 2

# Verificar si la cola está vacía
print(Cola.is_empty()) # Output: False

# Intentar eliminar un elemento de una cola vacía
Cola.dequeue()  # Elimina "Gatos"
Cola.dequeue()  # Elimina "Tortugas"
print(Cola.dequeue())  # La cola está vacía, Output: -1

# Verificar si la cola está vacía después de eliminar todos los elementos
print(Cola.is_empty()) # Output: True

# Intentar ver el elemento al frente de una cola vacía
print(Cola.peek())    # La cola está vacía, Output: -1

# Verificar el tamaño de la cola después de eliminar todos los elementos
print(Cola.size())    # Output: 0
