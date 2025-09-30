class HashTable:
    #Se inicializa con 10
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self,key):
        #Funcion hash de python
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        print("Clave no encontrada")
        return None
    
    def delete(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                print("Clave eliminada")
                return True
        print("Clave no encontrada")
        return False
    
    def display(self):
        for i, bucket in enumerate(self.table):
            if bucket:
                print(f"Índice {i}: {bucket}")
    
# Ejemplo de uso

# Numero de elementos pequeño para forzar colisiones
hash_table = HashTable(size=5)
hash_table.insert("nombre", "Juan")
hash_table.insert("edad", 30)
hash_table.insert("ciudad", "Madrid")
hash_table.insert("profesión", "Ingeniero")
hash_table.insert("hobby", "Fotografía")
hash_table.insert("deporte", "Fútbol")  # Se agregan 6 para probar colisiones
hash_table.display()                  # Muestra el contenido de la tabla hash

print(hash_table.search("nombre"))  # Output: "Juan"
hash_table.delete("edad")            # Output: "Clave eliminada"
print("Elementos en la tabla hash:", hash_table.size)             # Output: 5
hash_table.insert("profesión", "Programador")  # Actualiza el valor
hash_table.display()                  # Muestra el contenido de la tabla hash