def sortCandidates(g):
    candidates = []
    for adjs in g:
        for (start, end, weight) in adjs:
            candidates.append((weight, start, end))
    candidates.sort()
    return candidates

def actualizarComponente(componentes, nuevo, viejo):
    for i in range(0,len(componentes)):
        if componentes[i] == viejo:
            componentes[i] = nuevo

def vorazKruskal(grafo):
    solucion = 0
    candidatos = sortCandidates(grafo)
    listaComponentesTotales = list(range(len(grafo)))
    numComponentesTotales = len(listaComponentesTotales)
    i = 0
    costes = [0]*numComponentesTotales
    while numComponentesTotales > 1 and i < len(candidatos):
        (coste, origen, destino) = candidatos[i]
        if listaComponentesTotales[origen] != listaComponentesTotales[destino]:
            solucion = solucion + coste
            numComponentesTotales -= 1
            costes[origen] = costes[origen] + coste
            costes[destino] = costes[destino] + coste
            actualizarComponente(listaComponentesTotales, listaComponentesTotales[origen], listaComponentesTotales[destino])
        i = i + 1
    return [solucion, costes]

datos = input("").split(" ")
nodos = int(datos[0])
aristas = int(datos[1])

grafo = []
for _ in range(nodos):
    grafo.append([])

for i in range(aristas):
    datosAristas = input("").split(" ")
    origen = int(datosAristas[0])
    destino = int(datosAristas[1])
    coste = int(datosAristas[2])
    grafo[origen].append((origen, destino, coste))

[costeTotal, costeIndividual] = vorazKruskal(grafo)
for i in range(len(costeIndividual)):
    print(f"C{i} -> {costeIndividual[i]}")
print(f"Esfuerzo realizado -> {costeTotal}")
