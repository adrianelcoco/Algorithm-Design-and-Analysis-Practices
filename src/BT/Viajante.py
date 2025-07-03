import math

def mejorRuta(rutaA, rutaB):
    if rutaB[0] == -1:
        return True
    elif rutaA[0] == -1:
        return False
    else:
        totalA = calcularDistancia(rutaA)
        totalB = calcularDistancia(rutaB)
        return totalA < totalB

def calcularDistancia(ruta):
    distanciaTotal = 0.0
    for i in range(len(ruta) - 1):
        distanciaTotal += matrizDistancias[ruta[i]][ruta[i + 1]]
    distanciaTotal += matrizDistancias[ruta[-1]][ruta[0]]
    return distanciaTotal

def esFactible(ciudad, rutaActual, mejorRutaActual, visitado):
    if visitado[ciudad]:
        return False
    if mejorRuta(mejorRutaActual, rutaActual):
        return False
    return True

def clonarRuta(origen, destino):
    for i in range(len(origen)):
        destino[i] = origen[i]

def backtracking(ciudades, etapa, rutaActual, mejorRutaActual, visitado):
    for intento in range(1, ciudades):
        if esFactible(intento, rutaActual, mejorRutaActual, visitado):
            rutaActual[etapa] = intento
            visitado[intento] = True
            if etapa == ciudades - 1:
                if mejorRuta(rutaActual, mejorRutaActual):
                    clonarRuta(rutaActual, mejorRutaActual)
            else:
                backtracking(ciudades, etapa + 1, rutaActual, mejorRutaActual, visitado)
            rutaActual[etapa] = -1
            visitado[intento] = False

def obtenerDistancia(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

numCiudades = int(input())
x_coords = []
y_coords = []

for _ in range(numCiudades):
    x, y = map(float, input().split())
    x_coords.append(x)
    y_coords.append(y)

matrizDistancias = [[0.0 for _ in range(numCiudades)] for _ in range(numCiudades)]

for i in range(numCiudades):
    for j in range(i, numCiudades):
        distancia = obtenerDistancia(x_coords[i], y_coords[i], x_coords[j], y_coords[j])
        matrizDistancias[i][j] = matrizDistancias[j][i] = distancia

rutaActual = [-1] * numCiudades
rutaActual[0] = 0
mejorRutaEncontrada = [-1] * numCiudades
ciudadesVisitadas = [False] * numCiudades
ciudadesVisitadas[0] = True

backtracking(numCiudades, 1, rutaActual, mejorRutaEncontrada, ciudadesVisitadas)

mejorDistancia = calcularDistancia(mejorRutaEncontrada)
print("{:.4f}".format(mejorDistancia))
print(" ".join(map(str, mejorRutaEncontrada)))
