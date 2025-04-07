def estrategia_greedy(lista_famosos):
    tiempo_acumulado = 0
    tiempo_total = 0
    resultado = []
    #me guardo una tupla del famoso y el tiempo desde que empezo la entrevista
    for famoso in lista_famosos:
        resultado.append((famoso[0], tiempo_acumulado))
        tiempo_acumulado += famoso[3]
        tiempo_total += tiempo_acumulado

    return resultado


num_famosos = int(input(""))

famosos = []
for _ in range(num_famosos):
    datos = input("").split(" ")
    ratio = int(datos[1]) / int(datos[2])  # Calculamos la relación amabilidad/fama
    famosos.append((datos[0], int(datos[1]), int(datos[2]), int(datos[3]), ratio))

# Ordenamos por la relación amabilidad/fama de menor a mayor
famosos.sort(key=lambda x: x[4])

for famoso in famosos:
    print(famoso[0])

solucion = estrategia_greedy(famosos)

solucion.sort(key=lambda x: x[0])

print(solucion[0][1])

