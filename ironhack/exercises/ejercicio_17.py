# EJERCICIO 17
# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre
# por pantalla la frase invertida.

frase_usuario = input("Introduce una frase: ")
frase_invertida = ""
for character in frase_usuario:
    frase_invertida = character + frase_invertida
    print("La frase invertida es: ",frase_invertida)

    