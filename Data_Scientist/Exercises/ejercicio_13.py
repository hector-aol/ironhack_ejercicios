#Escribir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima 
#por pantalla en lineas distintas el nombre del usuario tantas veces como el numero intruducido.

nombre_usuario = int(input('Cual es tu nombre de usuario?: '))
numero_entero = int(input('Dime un numero entero: '))

for veces in range(numero_entero):
    print(nombre_usuario)

