def vorazGreedy(listaSeductores, tiempoMax, posCaracter):
    solucion = []
    beneficio = 0
    indice = 0
    while tiempoMax > 0 and indice < len(listaSeductores):
        seductor = listaSeductores[indice]
        indice = indice +1

        if tiempoMax >= seductor[4]:
            tiempoMax = tiempoMax - seductor[4]
            solucion.append((seductor[0]))
            beneficio = beneficio + seductor[posCaracter]
        else:
            solucion.append((seductor[0]))
            #(valorcandidato*tiempodisponible)/tiempototal
            beneficio += (seductor[posCaracter]*tiempoMax) / seductor[4]
            tiempoMax = 0

    print(*solucion)
    print(f"{beneficio:.2f}")


numConcursantes = int(input(""))
for i in range(numConcursantes):
    caracterMasImportante = input("")
    tiempoMaximo = int(input(""))
    totalCandidatos = int(input(""))
    candidatos = []
    for i in range(totalCandidatos):
        datos = input("").split(" ")
        if caracterMasImportante == "beauty":
            ratio = int(datos[1]) / int(datos[4])
            posCaracter = 1
        elif caracterMasImportante == "intelligence":
            ratio = int(datos[2]) / int(datos[4])
            posCaracter = 2
        else:
            ratio = int(datos[3]) / int(datos[4])
            posCaracter = 3
        candidatos.append((datos[0], int(datos[1]), int(datos[2]), int(datos[3]), int(datos[4]), ratio))
    candidatos = sorted(candidatos, key = lambda x: -x[5])
    vorazGreedy(candidatos, tiempoMaximo, posCaracter)

