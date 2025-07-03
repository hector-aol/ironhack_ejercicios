# Ejercicio 4. Lambda, map y filter
# Dada la siguiente lista de precios:
# precios = [125.5, 99.9, 50.0, 300.0, 75.25]
# Usa filter para obtener solo los precios mayores a 100, y luego map con lambda para aplicar un descuento del 15% a esos precios.
# Devuelve la nueva lista de precios con descuento.

precios = [125.5, 99.9, 50.0, 300.0, 75.25]
resultado = list(map(lambda p: p * 0.85, filter(lambda p: p > 100, precios)))
print("Precios con descuento del 15%:", resultado)
