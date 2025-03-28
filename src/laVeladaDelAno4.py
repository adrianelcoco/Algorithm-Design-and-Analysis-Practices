def vorazGreedy(listaActividdades, numeroDeActividades):
    horarioNuevo = [listaActividdades[0]]
    for i in range (1, numeroDeActividades):
        actividadCandidata = listaActividdades[i]
        ultimaActividad = horarioNuevo[len(horarioNuevo) - 1]
        if(actividadCandidata[1] >= ultimaActividad[2]):
            horarioNuevo.append(actividadCandidata)
    return len(horarioNuevo)

numActividades = int(input(""))
actividades = []

for i in range (numActividades):
    valores = input("").split(" ")
    actividades.append((valores[0],int(valores[1]),int (valores[2])))

actividades = sorted(actividades, key = lambda x: x[2])
solucion = vorazGreedy (actividades, numActividades)
print(solucion)