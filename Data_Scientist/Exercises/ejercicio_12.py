# EJERCICIOS 12
cantidad = int(input("Introduce el número de barras no frescas: "))
precio_original = 3.49
descuento_por_barra = precio_original * 0.60
precio_con_descuento = precio_original - descuento_por_barra
total = cantidad * precio_con_descuento
print(f"Precio habitual: {precio_original:.2f}€")
print(f"Descuento por barra no fresca: {descuento_por_barra:.2f}€")
print(f"Coste final total: {total:.2f}€")

