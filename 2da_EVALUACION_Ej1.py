import os

#Creacion de diccionario frutas, con nombre y precio
dic_frutas = {
    'platano':12,
    'manzana': 15,
    'uva': 20,
    'fresa': 25,
    'naranja': 18,
    'toronja': 20
}

#Ciclo para pedir frutas
while True:
    #Borrar lo que esta en consola
    os.system('cls')
    # Verificar si fruta esta en diccionario
    try: 
        # Pide fruta y guarda precio
        fruta = input('Ingresa nombre de fruta: ') 
        precio_individual = dic_frutas[fruta]
    except:
        # Si fruta no esta en diccionario, imprime y se va a la siguiente iteracion
        print('Fruta no existe...')
        print(f'Frutas disponibles:')
        i=1
        for keys, value in dic_frutas.items():
            print(f'{i}. {keys}')
            i+=1
        input('Presiona cualquier tecla para continuar')
        continue
    
    # Pedir cantidad
    cantidad = int(input('Ingresa cantidad: '))

    #Calcular precio final
    precio_final = precio_individual * cantidad

    #Imprimir precio Final
    print(f'\nPrecio final: {precio_final}')

    #Pedir si se quiere continuar
    opc = input("\nQuieres ingresar otra fruta ('S' si, 'N' no)")

    #Si no se quiere continuar, se sale del ciclo while
    if opc == 'N' or opc == 'n' :
        break

print('Fin de programa')

    