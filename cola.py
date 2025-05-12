class Cola:
    def __init__(self):
        self.items = []
    
    def encolar(self, item):
        self.items.append(item)
    
    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            print("La cola está vacía.")
            return None
    
    def ver_frente(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            print("La cola está vacía.")
            return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)
    
    def mostrar(self):
        print("Cola actual (frente a la izquierda):", self.items)