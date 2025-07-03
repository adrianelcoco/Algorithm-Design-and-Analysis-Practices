def contadorDeMonedas(lista):
    if len(lista) == 0:
        return (0,0)
    elif len(lista) == 1:
        if(isinstance(lista[0], list)):
            c = contadorDeMonedas(lista[0])
            return(c[0], c[1])
        else:
            return(lista[0], 1)

    else:
        if (isinstance(lista[0], list)):
            primerElem = contadorDeMonedas(lista[0])
            resto = contadorDeMonedas(lista[1:])
            return(primerElem[0] + resto[0], primerElem[1] + resto[1])
        else:
            resto = contadorDeMonedas(lista[1:])
            return (lista[0] + resto[0], 1+ resto[1])

lista = eval(input(""))
print(contadorDeMonedas(lista))