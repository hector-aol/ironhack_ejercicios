# EJERCICIO 16
#Los telefonos de una empresa tienen el siguiente formato <prefijo-numero-extension> donde el
#prefijo es el codigo del pais <+34>, y la extension tiene dos digitos (Por ejemplo: +34-913724710-56).
#Escribir un programa que pregunte por un numero de telefono con este formato y muestre por pantalla el numero de
#telefono sin el prefijo y la extension.

for var_1 in iter(int, 1):
#while True:
    telefono = input("Introduce un número de teléfono (formato: +34-XXXXXXXXX-XX): ")
#partes = telefono.split('-')
#numero_principal = partes[1]
#print('El numero principal es:', numero_principal)

    if telefono.count('-') == 2:
        partes = telefono.split('-')
        if len(partes[1]) >= 7:  
            numero_sin_prefijo_y_extension = partes[1]
            print("(Error de formato) sin prefijo ni extensión:", numero_sin_prefijo_y_extension)
            break
        else:
            print("Error de formato. Intenta de nuevo.")
    else:
        print("Formato incorrecto. Vuelve a intentarlo")

