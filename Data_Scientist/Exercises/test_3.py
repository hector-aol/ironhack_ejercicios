# alumnos = ["Ana", "Luis", "Pedro", "Sofía", "María", "Juan"]
# notas = [8.5, 4, 6.5, 9, 7, 3.5]

# a) crear el listado de notas en un conjunto inmutable
# notas_inmutables = alumnos + notas
# print("a) Notas inmutables:", notas_inmutables)

# alumnos = ["Ana", "Luis", "Pedro", "Sofía", "María", "Juan"]
# notas = [8.5, 4, 6.5, 9, 7, 3.5]
# # Crear listado usando bucle for
# listado = []
# for i in range(len(alumnos)):
#     listado.append((alumnos[i], notas[i]))

# # Mostrar resultado
# print("Listado completo:")
# for alumno, nota in listado:
#     #print(f"{alumno}: {nota}")
#     print(listado)
    

formato_linea = ", ".join([f"{alumno}:{nota}" for alumno, nota in listado])
print("Listado completo:", formato_linea)