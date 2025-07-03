# Ejercicio 9. Generación de informe 
# Con la estructura modificada del ejercicio anterior: 
# Guarda en un archivo llamado informe_usuarios.txt un resumen donde 
# cada línea tenga el siguiente formato: 
# usuario1 tiene 25 años - Mayor que promedio: False

lista_usuarios = [
    {'usuario': 'usuario1', 'edad': 25, 'mayor_que_promedio': False},
    {'usuario': 'usuario2', 'edad': 32, 'mayor_que_promedio': False},
    {'usuario': 'usuario4', 'edad': 45, 'mayor_que_promedio': True}
]

with open('informe_usuarios.txt', 'w') as f:
    f.writelines(
        f"{u['usuario']} tiene {u['edad']} años - Mayor que promedio: {u['mayor_que_promedio']}\n"
        for u in lista_usuarios
    )




# # Generar archivo de informe
# with open('informe_usuarios.txt', 'w') as archivo:
#     for usuario in lista_usuarios:
#         # Formatear línea según especificación
#         linea = f"{usuario['usuario']} tiene {usuario['edad']} años - Mayor que promedio: {usuario['mayor_que_promedio']}\n"
#         archivo.write(linea)

# print("Informe generado en 'informe_usuarios.txt'")

# # Opcional: leer y mostrar el contenido generado
# print("\nContenido del informe:")
# with open('informe_usuarios.txt', 'r') as archivo:
#     print(archivo.read())