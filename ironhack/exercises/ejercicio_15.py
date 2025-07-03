# EJERCICIO 15
# Escribir un programa que pregunte el nombre del usuario en la consola y despues de que el usuario
# lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, en donde <NOMBRE> es el nombre de usuario
# en mayusculas y <n> es el nombre de letras que tiene el nombre.

nombre_usuario = input("Cual es tu nombre de usuario?: ")
nombre_usuario_mayusculas = nombre_usuario.upper()
#contador_solamente_letras = (1 for character in nombre_usuario if character.isalpha())
#print(nombre_usuario_mayusculas,"tiene", contador_solamente_letras,"letras.")

contador_letras = 0
indice = 0

while indice < len(nombre_usuario):
    if nombre_usuario[indice].isalpha():
        contador_letras += 1
    indice += 1
print(f"{nombre_usuario_mayusculas} tiene {contador_letras} letras.")
