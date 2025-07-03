# Ejercicio 8. Transformación avanzada
# A partir de la lista de diccionarios del ejercicio anterior:
# Usa reduce para obtener la suma total de edades.
# Calcula la edad promedio (usa len()).
# Añade una nueva clave a cada diccionario llamada "mayor_que_promedio" (valor booleano) que indique si el usuario tiene más edad 
# que la media.

from functools import reduce

# Lista de ejemplo (obtenida del ejercicio anterior)
lista_usuarios = [
    {'usuario': 'usuario1', 'edad': 25},
    {'usuario': 'usuario2', 'edad': 32},
    {'usuario': 'usuario4', 'edad': 45}
]

# 1. Calcular suma total de edades usando reduce
suma_edades = reduce(lambda acum, usuario: acum + usuario['edad'], lista_usuarios, 0)

# 2. Calcular edad promedio
promedio = suma_edades / len(lista_usuarios) if lista_usuarios else 0

# 3. Añadir nueva clave 'mayor_que_promedio'
for usuario in lista_usuarios:
    usuario['mayor_que_promedio'] = usuario['edad'] > promedio

# Mostrar resultados
print(f"Suma total de edades: {suma_edades}")
print(f"Edad promedio: {promedio:.2f}")
print("\nLista actualizada:")
for usuario in lista_usuarios:
    print(usuario)

    