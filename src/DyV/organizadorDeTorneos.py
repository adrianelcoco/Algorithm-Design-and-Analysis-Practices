def mergeSortTorneo(puntuaciones, inicio, final):
    if inicio == final:
        return [puntuaciones[inicio]], 0
    else:
        mitad = (inicio + final) // 2
        vectorOrdenado1, movimientos1 = mergeSortTorneo(puntuaciones, inicio, mitad)
        vectorOrdenado2, movimientos2 = mergeSortTorneo(puntuaciones, mitad + 1, final)
        i = 0
        j = 0
        acum = 0
        vectorOrdenadoFinal = []
        while i < len(vectorOrdenado1) and j < len(vectorOrdenado2):
            if vectorOrdenado1[i] < vectorOrdenado2[j]:
                vectorOrdenadoFinal.append(vectorOrdenado1[i])
                i += 1
            else:
                vectorOrdenadoFinal.append(vectorOrdenado2[j])
                j += 1
                acum = acum + (len(vectorOrdenado1) - i)

        while i < len(vectorOrdenado1):
            vectorOrdenadoFinal.append(vectorOrdenado1[i])
            i += 1
        while j < len(vectorOrdenado2):
            vectorOrdenadoFinal.append(vectorOrdenado2[j])
            j += 1
        return vectorOrdenadoFinal, movimientos1 + movimientos2 + acum


numTotalPuntuaciones = int(input())
puntuaciones = input().split()
listaP = []
for puntuacion in puntuaciones:
    listaP.append(int(puntuacion))
vectoFinal, movimientos = mergeSortTorneo(puntuaciones, 0, len(listaP) - 1)
print(movimientos)