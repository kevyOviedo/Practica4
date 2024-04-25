#-- almacenar nombre e identificacion de personas con diccionarios
dictionary = {}
i=0
while True:
    print("\nEscribe 'exit' para salir")
    entrada = input("Ingresa id y nombre de la persona. Formato: 'id' , 'nombre'\n")

    entrada = entrada.split(',')

    if entrada[0]=='exit':
        break
    
    dictionary[entrada[0]] = entrada[1]

print('ID | NOMBRE')
for item in dictionary:
    print(f'{item} : {dictionary[item]} ')
    i+=1

#a
