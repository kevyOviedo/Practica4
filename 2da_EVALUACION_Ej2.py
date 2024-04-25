import random
import os

#Funcion para generar lista de numeros aleatorios
def generarLista(n):
    lista = []
    # Generar 'size' numeros aleatorios y agregarlos a lista
    for i in range(n):
        lista.append(random.randint(1,1000))

    return lista
#Funcion para generar dic con lista^2
def generarDic(lista,n):
    dic = {}
    # Se agrega a diccionario valor con llave i de 1 hasta size, y valor lista[i]^2
    for i in range(n):
        dic[i] = lista[i]**2
    
    return dic
#Funcion para pedir tamano de lista
def pedirSize():

    #Ciclo para validar que entrada sea numero
    while True:
        os.system('cls')
        # se pide entrada, y se intenta ahcer int
        try:
            size = int(input('Ingresa el tamano de lista: \n'))
        #Si no es un numero, da error y se continua la siguiente iteracion
        except:
            print('Entrada no es un numero...\n')
            input('Presiona cualquier tecla para continuar')
            continue
        # Se sale del ciclo
        break
    return size

while True:
    #Limpiar pantalla
    os.system('cls')

    #Mandar llamar funcion pedirSize()
    size = pedirSize()

    # Se manda a llamar la funcion para generarLista() de tamano size y se guarda en 'lista'
    lista = generarLista(size)
    # Se manda a llamar la funcion generarDic(), mandando a la lista y el tamano como parametros. Se guarda en 'dic'
    dic = generarDic(lista, size)

    #Imprimir lista y dic
    print(f'\nLista de numero aleatorios: {lista}\n')
    print(f'Diccionario con lista^2: {dic}\n')

    #Pedir si se quiere continuar
    opc = input("\nQuieres volver a ejecutar el programa? ('S' si, 'N' no)")

    #Si no se quiere continuar, se sale del ciclo while
    if opc == 'N' or opc == 'n' :
        break

print('Fin de programa')