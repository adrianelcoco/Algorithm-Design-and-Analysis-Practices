def mirrorRecursivo(entrada):
    if len(entrada) == 1 or len(entrada) == 0:
        return entrada
    else:
        return mirrorRecursivo(entrada[1:]) + entrada[0]


def mirrorRecursivo2(entrada):
    if len(entrada) > 1:
        return entrada[-1] + mirrorRecursivo2(entrada[0:(len(entrada) - 1)])
    else:
        return entrada


entrada = input("")
print(mirrorRecursivo2(entrada))