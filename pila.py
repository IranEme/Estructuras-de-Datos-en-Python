class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self, item):
        self.items.append(item)
    
    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía.")
            return None
    
    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            print("La pila está vacía.")
            return None
    
    def esta_vacia(self):
        return len(self.items) == 0
    
    def tamano(self):
        return len(self.items)
    
    def mostrar(self):
        print("Pila actual (tope a la derecha):", self.items)