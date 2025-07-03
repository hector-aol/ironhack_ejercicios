# EJERCICIO 20
# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales
# y muestre por pantalla el numero de euros y el numero de centimos del precio introducido.

precio_euros = input("Introduce el precio del producto en euros (con dos decimales): ")

# Convertir el precio a un número de punto flotante (float)
precio = float(precio_euros)

euros = int(precio)  # La parte entera del precio son los euros
centimos = round((precio - euros) * 100)  # Calcular los céntimos

print("Euros:", euros)
print("Céntimos:", centimos)

