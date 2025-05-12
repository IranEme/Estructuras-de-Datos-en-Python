class MiDiccionario:
    def __init__(self, tamano=10):
        self.tamano = tamano
        self.tabla = [[] for _ in range(tamano)]  # Lista de listas para manejar colisiones
    
    def _hash(self, clave):
        return hash(clave) % self.tamano
    
    def agregar(self, clave, valor):
        indice = self._hash(clave)
        
        # Buscar si la clave ya existe para actualizarla
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)
                return
        
        # Si la clave no existe, agregarla
        self.tabla[indice].append((clave, valor))
    
    def obtener(self, clave):
        indice = self._hash(clave)
        
        # Buscar la clave en la lista de la posición hash
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        
        # Si no se encuentra la clave
        raise KeyError(f"La clave '{clave}' no se encuentra en el diccionario")
    
    def eliminar(self, clave):
        indice = self._hash(clave)
        
        # Buscar y eliminar la clave
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                del self.tabla[indice][i]
                return
        
        # Si no se encuentra la clave
        raise KeyError(f"La clave '{clave}' no se encuentra en el diccionario")
    
    def contiene(self, clave):
        indice = self._hash(clave)
        
        for k, _ in self.tabla[indice]:
            if k == clave:
                return True
        
        return False
    
    def claves(self):
        todas_claves = []
        for casilla in self.tabla:
            for k, _ in casilla:
                todas_claves.append(k)
        return todas_claves
    
    def valores(self):
        todos_valores = []
        for casilla in self.tabla:
            for _, v in casilla:
                todos_valores.append(v)
        return todos_valores
    
    def mostrar(self):
        print("Contenido del diccionario:")
        for i, casilla in enumerate(self.tabla):
            if casilla:  # Solo mostrar casillas no vacías
                print(f"Índice {i}: {casilla}")