
lis = ["lili","juan","jose","luis","josue","Jorge","Ana"]
l = [8,4,2,5,6,6,7,3,3,4]
for x in l:
    print (f'Nombre : {x}')
for x in range(len(lis)):
    print (f'numero de lista : {x}')



def completar_lista(lista):
    repetidos = []
    resultado = []

    for numero in lista:
        if numero not in resultado:
            resultado.append(numero)
        else:
            repetidos.append(numero)

    numeros_faltantes = set(range(1, 115)) - set(resultado)
    numeros_faltantes = sorted(list(numeros_faltantes))

    for numero in repetidos:
        resultado.append(numeros_faltantes.pop(0))

    return resultado
