def contar_monedas(lista):
    if not lista:
        return 0, 0
    primero = lista[0]
    resto = lista[1:]
    if isinstance(primero, list):
        suma_primero, cantidad_primero = contar_monedas(primero)
    else:
        suma_primero, cantidad_primero = primero, 1
    suma_resto, cantidad_resto = contar_monedas(resto)
    return suma_primero + suma_resto, cantidad_primero + cantidad_resto

datos = eval(input(""))
print(contar_monedas(datos))