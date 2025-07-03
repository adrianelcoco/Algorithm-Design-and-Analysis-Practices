def caminoMinimo(distancias, visitados):
    mejorNodo = None
    distanciaMinima = float('inf')
    for i in range(len(distancias)):
        if(not visitados[i] and distancias[i] < distanciaMinima):
            distanciaMinima = distancias[i]
            mejorNodo = i
    return mejorNodo

def vorazDijkstra (grafo, nodoOrigen):
    distancias = []
    precedencias = []
    visitados = []
    for i in range (len(grafo)):
        distancias.append(float('inf'))
        precedencias.append(None)
        visitados.append(False)
    distancias[nodoOrigen] = 0
    visitados[nodoOrigen] = True

    for (origen, destino, coste) in grafo[nodoOrigen]:
        distancias[destino] = coste
        precedencias[destino] = origen

    for i in range(1, len(grafo)):
        mejorNodo = caminoMinimo(distancias, visitados)
        visitados[mejorNodo] = True
        for (origen, destino, coste) in grafo[mejorNodo]:
            valorDistanciaAntiguo = distancias[destino]
            mejorDistancia = min(valorDistanciaAntiguo, distancias[origen] + coste)
            if valorDistanciaAntiguo != mejorDistancia:
                distancias[destino] = mejorDistancia
                precedencias[destino] = mejorNodo

    return precedencias, distancias


datos = input("").split(" ")
nodos = int(datos[0])
aristas = int(datos[1])
grafo = []
for i in range(nodos):
    grafo.append([])
for i in range(aristas):
    datosAristas = input("").split(" ")
    origen = int(datosAristas[0])
    destino = int(datosAristas[1])
    coste = int(datosAristas[2])
    grafo[origen].append((origen, destino, coste))
    grafo[destino].append((destino, origen, coste))

datosFinales = input("").split(" ")
nodoOrigen = int(datosFinales[0])
nodoDestino= int(datosFinales[1])

precedencia, distancias = vorazDijkstra(grafo, nodoOrigen)

print(distancias[nodoDestino])
listaRecorrido = []
while nodoDestino is not None:
    listaRecorrido.append(nodoDestino)
    nodoDestino = precedencia[nodoDestino]
listaRecorrido.reverse()
print(*listaRecorrido)
