# Ejercicio 22
# Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# separados por comas, y muestre por pantalla cada uno de los productos en una linea distinta.

# Preguntar por los productos de la cesta de la compra
productos_texto = input("Introduce los productos de la cesta de la compra separados por comas: ")

# Dividir la cadena de texto en una lista de productos
productos = productos_texto.split(',')

# Mostrar cada producto en una línea distinta
for producto in productos:
    print(producto.strip())  # .strip() elimina espacios en blanco al principio y al final
