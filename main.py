from estructuras import MiLista
from pila import Pila
from cola import Cola
from arbol import ArbolBinario
from diccionario import MiDiccionario

def probar_lista():
    print("\n=== PROBANDO LISTA ===")
    mi_lista = MiLista()
    mi_lista.agregar(10)
    mi_lista.agregar(20)
    mi_lista.agregar(30)
    mi_lista.mostrar()
    
    print("Agregando en posición 1:")
    mi_lista.agregar_en_posicion(1, 15)
    mi_lista.mostrar()
    
    print("Eliminando elemento 20:")
    mi_lista.eliminar(20)
    mi_lista.mostrar()
    
    print("Eliminando en posición 0:")
    elemento = mi_lista.eliminar_en_posicion(0)
    print(f"Elemento eliminado: {elemento}")
    mi_lista.mostrar()
    
    print(f"Longitud de la lista: {mi_lista.longitud()}")
    print(f"¿Está vacía? {mi_lista.esta_vacia()}")
    print(f"¿Contiene 15? {mi_lista.buscar(15)}")
    print(f"¿Contiene 50? {mi_lista.buscar(50)}")
    
    indice = mi_lista.obtener_indice(15)
    print(f"Índice de 15: {indice}")
    
    mi_lista.agregar(5)
    mi_lista.mostrar()
    
    print("Lista ordenada:")
    mi_lista.ordenar()
    mi_lista.mostrar()
    
    print("Lista invertida:")
    mi_lista.invertir()
    mi_lista.mostrar()

def probar_pila():
    print("\n=== PROBANDO PILA ===")
    pila = Pila()
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    pila.mostrar()
    
    print(f"Tope: {pila.ver_tope()}")
    print(f"Tamaño: {pila.tamano()}")
    
    print("Desapilando elementos:")
    print(f"Elemento desapilado: {pila.desapilar()}")
    pila.mostrar()
    
    print(f"Elemento desapilado: {pila.desapilar()}")
    pila.mostrar()
    
    print(f"Elemento desapilado: {pila.desapilar()}")
    pila.mostrar()
    
    # Intentar desapilar de una pila vacía
    pila.desapilar()

def probar_cola():
    print("\n=== PROBANDO COLA ===")
    cola = Cola()
    cola.encolar(10)
    cola.encolar(20)
    cola.encolar(30)
    cola.mostrar()
    
    print(f"Frente: {cola.ver_frente()}")
    print(f"Tamaño: {cola.tamano()}")
    
    print("Desencolando elementos:")
    print(f"Elemento desencolado: {cola.desencolar()}")
    cola.mostrar()
    
    print(f"Elemento desencolado: {cola.desencolar()}")
    cola.mostrar()
    
    print(f"Elemento desencolado: {cola.desencolar()}")
    cola.mostrar()
    
    # Intentar desencolar de una cola vacía
    cola.desencolar()

def probar_arbol():
    print("\n=== PROBANDO ÁRBOL BINARIO ===")
    arbol = ArbolBinario()
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)
    
    print("Recorridos del árbol:")
    arbol.mostrar()
    
    print(f"¿Existe 40 en el árbol? {arbol.buscar(40)}")
    print(f"¿Existe 90 en el árbol? {arbol.buscar(90)}")

def probar_diccionario():
    print("\n=== PROBANDO DICCIONARIO ===")
    diccionario = MiDiccionario()
    diccionario.agregar("uno", 1)
    diccionario.agregar("dos", 2)
    diccionario.agregar("tres", 3)
    
    # Provocar una colisión (aunque es difícil garantizarla)
    diccionario.agregar("catorce", 14)
    diccionario.agregar("veinticinco", 25)
    
    diccionario.mostrar()
    
    print(f"Valor de 'dos': {diccionario.obtener('dos')}")
    
    print("Eliminando 'tres'...")
    diccionario.eliminar("tres")
    
    print(f"¿Contiene 'tres'? {diccionario.contiene('tres')}")
    print(f"¿Contiene 'dos'? {diccionario.contiene('dos')}")
    
    print(f"Claves: {diccionario.claves()}")
    print(f"Valores: {diccionario.valores()}")
    
    # Intentar acceder a una clave que no existe
    try:
        diccionario.obtener("cuatro")
    except KeyError as e:
        print(f"Error esperado: {e}")

if __name__ == "__main__":
    probar_lista()
    probar_pila()
    probar_cola()
    probar_arbol()
    probar_diccionario()