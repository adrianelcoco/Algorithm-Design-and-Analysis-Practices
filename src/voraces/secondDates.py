
def vorazGreedy(participantes, tamGrupo, numParticipantes):
    jovenes = []
    no_jovenes = []
    restoGrupo = numParticipantes - tamGrupo
    minGrupo = min(tamGrupo, restoGrupo)
    while minGrupo > 0:
        jovenes.append(participantes[0])
        no_jovenes.insert(0, participantes[len(participantes) - 1])
        participantes.pop(0)
        participantes.pop(len(participantes) - 1)
        minGrupo -= 1
    for i in range(len(participantes)):
        no_jovenes.insert(0,participantes[len (participantes)- 1 - i])

    for joven in jovenes:
        print(joven[0], end=" ")
    print("")
    for noJoven in no_jovenes:
        print(noJoven[0], end=" ")
    print("")

(numParticipantes, tamGrupo) = input("").split(" ")
numParticipantes = int(numParticipantes)
tamGrupo = int(tamGrupo)
participantes = []
for i in range(numParticipantes):
    datos = input("").split(" ")
    participantes.append((datos[0], int(datos[1])))

participantes = sorted(participantes, key = lambda x: x[1])
vorazGreedy(participantes, tamGrupo, numParticipantes)