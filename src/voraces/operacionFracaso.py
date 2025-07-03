from collections import deque

def recorridoFamoso(grafo, nota):
    visitados = set()
    cola = deque()
    cola.append((0, nota))
    visitados.add(0)
    while cola:
        nodo, nota = cola.popleft()
        if nota == 1:
            continue

        for vecino in grafo[nodo]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, nota - 1))

    return (len(visitados))

numConcursante = int(input(""))
for _ in range(numConcursante):
    datos = input("").split(" ")
    nota = int(datos[0])
    nodos = int(datos[1])
    grafo = []
    for _ in range(nodos):
        grafo.append([])
    aristas = int(datos[2])
    for _ in range(aristas):
        conexiones = input("").split(" ")
        origen = int(conexiones[0])
        destino = int(conexiones[1])
        grafo[origen].append((destino))
        grafo[destino].append((origen))

    print(recorridoFamoso(grafo, nota))

