# Ejercicio 7. Filtrado y modificación
# Con el diccionario del ejercicio anterior:
# Usa filter para obtener solo los usuarios mayores o iguales a 18 años.
# Usa map o comprensión de listas para construir una lista de diccionarios con la estructura:
# [{'usuario': 'usuario1', 'edad': 25}, {'usuario': 'usuario2', 'edad': 32}]

lista_resultado = [
    {'usuario': u, 'edad': e} 
    for u, e in filter(lambda x: x[1] >= 18, usuarios_edades.items())
]

# # Suponiendo que tenemos el diccionario del ejercicio anterior
# # Ejemplo de diccionario (reemplazar con el resultado real del Ejercicio 6)
# usuarios_edades = {
#     "usuario1": 25,
#     "usuario2": 32,
#     "usuario3": 17,
#     "usuario4": 45,
#     "usuario5": 16
# }

# # 1. Filtrar usuarios mayores o iguales a 18 años usando filter
# usuarios_filtrados = filter(lambda item: item[1] >= 18, usuarios_edades.items())

# # 2. Convertir a lista (filter devuelve un iterador)
# lista_filtrada = list(usuarios_filtrados)

# # 3. Construir lista de diccionarios usando comprensión de listas
# lista_resultado = [
#     {'usuario': usuario, 'edad': edad}
#     for usuario, edad in lista_filtrada
# ]

# # Versión alternativa todo en uno (sin paso intermedio):
# # lista_resultado = [
# #     {'usuario': usuario, 'edad': edad}
# #     for usuario, edad in filter(lambda item: item[1] >= 18, usuarios_edades.items())
# # ]

# # Mostrar resultado
# print("Usuarios mayores de edad:")
# print(lista_resultado)