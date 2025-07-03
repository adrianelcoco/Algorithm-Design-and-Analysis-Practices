def mochilaDoble(pesos, asignacion, cargaActual, limite1, limite2, mejorAsignacion, mejorCarga, nivel):
    opcion = 0
    while opcion < 3:
        if opcion == 0:
            asignacion[nivel] = opcion
            if nivel == len(asignacion) - 1:
                if sum(mejorCarga) < sum(cargaActual):
                    mejorAsignacion[:] = asignacion[:]
                    mejorCarga[0] = cargaActual[0]
                    mejorCarga[1] = cargaActual[1]
            else:
                mochilaDoble(pesos, asignacion, cargaActual, limite1, limite2, mejorAsignacion, mejorCarga, nivel + 1)

        elif opcion == 1:
            if cargaActual[0] + pesos[nivel] <= limite1:
                asignacion[nivel] = opcion
                cargaActual[0] += pesos[nivel]
                if nivel == len(asignacion) - 1:
                    if sum(mejorCarga) < sum(cargaActual):
                        mejorAsignacion[:] = asignacion[:]
                        mejorCarga[0] = cargaActual[0]
                        mejorCarga[1] = cargaActual[1]
                else:
                    mochilaDoble(pesos, asignacion, cargaActual, limite1, limite2, mejorAsignacion, mejorCarga, nivel + 1)
                cargaActual[0] -= pesos[nivel]
                asignacion[nivel] = 0

        else:
            if cargaActual[1] + pesos[nivel] <= limite2:
                asignacion[nivel] = opcion
                cargaActual[1] += pesos[nivel]
                if nivel == len(asignacion) - 1:
                    if sum(mejorCarga) < sum(cargaActual):
                        mejorAsignacion[:] = asignacion[:]
                        mejorCarga[0] = cargaActual[0]
                        mejorCarga[1] = cargaActual[1]
                else:
                    mochilaDoble(pesos, asignacion, cargaActual, limite1, limite2, mejorAsignacion, mejorCarga, nivel + 1)
                cargaActual[1] -= pesos[nivel]
                asignacion[nivel] = 0

        opcion += 1

numObjetos = int(input())
pesosObjetos = list(map(int, input().split()))
capacidad1, capacidad2 = map(int, input().split())

asignacionActual = [0] * numObjetos
cargaActual = [0, 0]
mejorAsignacion = [0] * numObjetos
mejorCarga = [0, 0]

mochilaDoble(pesosObjetos, asignacionActual, cargaActual, capacidad1, capacidad2, mejorAsignacion, mejorCarga, 0)

print(sum(mejorCarga))
