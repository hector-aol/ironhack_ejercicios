# Ejercicio 5. Iteración sobre diccionarios
# Crea un diccionario con los nombres y edades de 5 personas. Luego:
# Usa un bucle para imprimir solo las personas mayores de edad.
# Devuelve una nueva lista con strings del tipo "Nombre (Edad años)" para los mayores de edad, usando zip,
# comprensión de listas y items().

personas = {"Juan": 25, "Ana": 17, "Luis": 30, "Marta": 16, "Pedro": 22}

# Imprimir mayores
print("Personas mayores de edad:")
[print(f"- {nombre}: {edad} años") for nombre, edad in personas.items() if edad >= 18]

# Crear lista formateada
lista_final = [
    f"{nombre} ({edad} años)" 
    for nombre, edad in zip(
        [n for n, e in personas.items() if e >= 18],
        [e for n, e in personas.items() if e >= 18]
    )
]

print("\nLista formateada de mayores de edad:")
print(lista_final)