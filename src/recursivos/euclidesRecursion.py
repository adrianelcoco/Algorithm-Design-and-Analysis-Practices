def euclidesRecursivo(a, b):
    if b == 0:
        return a
    else:
        resto = a%b
        return euclidesRecursivo(b, resto)

datos = input("").split(" ")
a = int(datos[0])
b = int(datos[1])
resultado = euclidesRecursivo(a, b)
print(resultado)

