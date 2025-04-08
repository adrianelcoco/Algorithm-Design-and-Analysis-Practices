def vorazGreedy(listaOrganizacion, numOrganizacion):
    solucion = []
    solucion.append(listaOrganizacion[0])
    finalAnterior = listaOrganizacion[0][1]
    total = 1
    for i in range(numOrganizacion):
        inicio = listaOrganizacion[i][0]
        if finalAnterior <= inicio:
            solucion.append(listaOrganizacion[i])
            total += 1
            finalAnterior = listaOrganizacion[i][1]

    print (total)

numOrganizaciones = int(input(""))

for i in range(numOrganizaciones):
    listaOrganizaciones = []
    numOrganizacion =  int(input(""))
    datos = input("").split(" ")
    numViajes = 0
    while numViajes < len(datos):
        listaOrganizaciones.append((int(datos[numViajes]), int(datos[numViajes+1])))
        numViajes +=2

    listaOrganizaciones = sorted(listaOrganizaciones, key = lambda x: x[1])
    vorazGreedy(listaOrganizaciones, numOrganizacion)
