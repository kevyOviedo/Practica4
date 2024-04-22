#-- almacenar nombre e identificacion de personas con tablas
tabla = [[],[]]
i=0
while True:
    print("\nEscribe 'exit' para salir")
    entrada = input("Ingresa id y nombre de la persona. Formato: 'id' , 'nombre'\n")

    entrada = entrada.split(',')

    if entrada[0]=='exit':
        break
    
    tabla[0].append(entrada[0])
    tabla[1].append(entrada[1])

print('ID | NOMBRE')
for item in tabla[0]:
    print(f'{item} : {tabla[1][i]}')
    i+=1

