# EJERCICIO 23
# Escribir un programa que pregunte el nombre de un producto, precio y numero de unidades.
# Y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con
# 6 digitos enteros y 2 digitos decimales, el numero de unidades con tres digitos y el coste total con 8 digitos enteros y 2 numeros decimales.

# Solicitar datos al usuario
nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

# Calcular el coste total
total = precio * unidades

# Formatear los valores según especificaciones
precio_formateado = f"{precio:09.2f}"  # 9 caracteres: 6 enteros + punto + 2 decimales
unidades_formateadas = f"{unidades:03d}"  # 3 dígitos con ceros a la izquierda
total_formateado = f"{total:011.2f}"  # 11 caracteres: 8 enteros + punto + 2 decimales

# Mostrar resultados
print(f"{nombre}: {precio_formateado} € x {unidades_formateadas} = {total_formateado} €")