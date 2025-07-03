def dyvClearSouls(vectorEnemigos, inicio, final, nivelMax):
    if inicio > final:
        return inicio
    else:
        mitad = (inicio + final) // 2
        if vectorEnemigos[mitad] <= nivelMax:
            return dyvClearSouls(vectorEnemigos, mitad+1, final, nivelMax)
        else:
            return dyvClearSouls(vectorEnemigos, inicio, mitad - 1, nivelMax)

numEnemigos = int(input())
vectorEnemigos = []
acum = 0
enemigos = input().split()
for enemigo in enemigos:
    vectorEnemigos.append(int(enemigo))
numPruebas = int(input())
for i in range(numPruebas):
    nivelMax = int(input())
    posicion = dyvClearSouls(vectorEnemigos, 0, len(vectorEnemigos) - 1, nivelMax)
    print(f"{posicion} {sum(vectorEnemigos[:posicion])}")

