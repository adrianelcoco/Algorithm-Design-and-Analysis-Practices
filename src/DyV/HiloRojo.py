def busqBinHR(g, inicio, final, id):
    if inicio == final:
        if g[inicio] == id:
            return inicio
        else:
            return -1
    else:
        mitad = (inicio + final) //2
        if g[mitad] == id:
            return mitad
        elif g[mitad] < id:
            return busqBinHR(g, mitad+1, final, id)
        else:
            return busqBinHR(g, inicio, mitad, id)

numG1 = int(input())
g1 = []
persG1 = input().split()
for pers in persG1:
    g1.append(int(pers))
numG2 = int(input())
g2 = []
persG2 = input().split()
for pers in persG2:
    g2.append(int(pers))
numPruebas = int(input())
listaIDs = []
for _ in range(numPruebas):
    ids = input().split()
    id1 = int(ids[0])
    id2 = int(ids[1])
    estaEnLista1 = busqBinHR(g1, 0, len(g1) - 1, id1)
    estaEnLista2 = busqBinHR(g2, 0, len(g2) - 1, id2)
    if estaEnLista1 != -1 and estaEnLista2 != -1:
        print(estaEnLista1, estaEnLista2)
    else:
        print("SIN DESTINO")

