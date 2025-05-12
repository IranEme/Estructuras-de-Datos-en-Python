class MiLista:
    def __init__(self):
        self.lista = []
    
    def agregar(self, elemento):
        self.lista.append(elemento)
    
    def agregar_en_posicion(self, posicion, elemento):
        if 0 <= posicion <= len(self.lista):
            self.lista.insert(posicion, elemento)
        else:
            print(f"Posición {posicion} fuera de rango.")
    
    def eliminar(self, elemento):
        if elemento in self.lista:
            self.lista.remove(elemento)
            return True
        else:
            print(f"{elemento} no encontrado en la lista.")
            return False
    
    def eliminar_en_posicion(self, posicion):
        if 0 <= posicion < len(self.lista):
            elemento = self.lista.pop(posicion)
            return elemento
        else:
            print(f"Posición {posicion} fuera de rango.")
            return None
    
    def mostrar(self):
        print("Lista actual:", self.lista)
    
    def buscar(self, elemento):
        return elemento in self.lista
    
    def obtener_indice(self, elemento):
        try:
            return self.lista.index(elemento)
        except ValueError:
            print(f"{elemento} no encontrado en la lista.")
            return -1
    
    def obtener_elemento(self, posicion):
        if 0 <= posicion < len(self.lista):
            return self.lista[posicion]
        else:
            print(f"Posición {posicion} fuera de rango.")
            return None
    
    def longitud(self):
        return len(self.lista)
    
    def esta_vacia(self):
        return len(self.lista) == 0
    
    def limpiar(self):
        self.lista.clear()
    
    def ordenar(self):
        self.lista.sort()
    
    def invertir(self):
        self.lista.reverse()