from collections import deque

def num_componentes_conexas(grafo, num_nodos):
    num_conexas = 0
    visitados = set()
    for nodo in range(num_nodos):
        if nodo not in visitados:
            num_conexas += 1
            cola = deque()
            visitados.add(nodo)
            cola.append(nodo)
            while cola:
                actual = cola.popleft()
                for vecino in grafo[actual]:
                    if vecino not in visitados:
                        visitados.add(vecino)
                        cola.append(vecino)
    return num_conexas

datos = input("").split(" ")
numNodos = int(datos[0])
numAristas = int(datos[1])
grafo = []
for i in range(numNodos):
    grafo.append([])
for j in range(numAristas):
    datosAristas = input("").split(" ")
    origen = int(datosAristas[0])
    destino = int(datosAristas[1])
    grafo[origen].append(destino)
    grafo[destino].append(origen)
sol = num_componentes_conexas(grafo, numNodos)
print(sol)
