class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)
    
    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
    
    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)
    
    def _buscar_recursivo(self, nodo, valor):
        if nodo is None:
            return False
        
        if nodo.valor == valor:
            return True
        
        if valor < nodo.valor:
            return self._buscar_recursivo(nodo.izquierda, valor)
        else:
            return self._buscar_recursivo(nodo.derecha, valor)
    
    def recorrido_inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._inorden_recursivo(nodo.derecha, resultado)
    
    def recorrido_preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorden_recursivo(nodo.izquierda, resultado)
            self._preorden_recursivo(nodo.derecha, resultado)
    
    def recorrido_postorden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierda, resultado)
            self._postorden_recursivo(nodo.derecha, resultado)
            resultado.append(nodo.valor)
    
    def mostrar(self):
        if self.raiz is None:
            print("El árbol está vacío")
            return
        
        print("Recorrido inorden:", self.recorrido_inorden())
        print("Recorrido preorden:", self.recorrido_preorden())
        print("Recorrido postorden:", self.recorrido_postorden())