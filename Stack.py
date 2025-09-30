class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.is_empty():
            print("El stack está vacío")
            return -1
        popped_node = self.top
        self.top = self.top.next
        self.count -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("El stack está vacío")
            return -1
        return self.top.data
    
    def size(self):
        return self.count

# Ejemplo de uso

# Crear una instancia de Stack
MyStack = Stack()

# Agreagar elementos al stack
MyStack.push(10)
MyStack.push(20)
MyStack.push(30)

# Eliminar y ver elementos del stack
print(MyStack.pop())  # Output: 30

# Ver el elemento en la cima del stack
print(MyStack.peek()) # Output: 20

# Verificar el tamaño del stack y si está vacío
print(MyStack.size()) # Output: 2
print(MyStack.is_empty()) # Output: False

# Intentar eliminar un elemento de un stack vacío
MyStack.pop()  # Elimina 20
MyStack.pop()  # Elimina 10
print(MyStack.pop())  # Output: El stack está vacío \n -1

# Intentar ver el elemento en la cima de un stack vacío
print(MyStack.peek()) # Output: El stack está vacío \n -1

# Verificar el tamaño del stack y si está vacío
print(MyStack.size()) # Output: 0
print(MyStack.is_empty()) # Output: True
