# EJERCICIO 21
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa
# y muestra por pantalla el dia, mes y año. Adaptar el programa anterior para que tambien funcione
# cuando el dia o el mes se introduzcan con un solo caracter.

# Preguntar al usuario la fecha de nacimiento en formato dd/mm/aaaa
fecha_nacimiento = input("Introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

# Dividir la fecha en día, mes y año
partes_fecha = fecha_nacimiento.split('/')

# Extraer día, mes y año
dia = partes_fecha[0]
mes = partes_fecha[1]
año = partes_fecha[2]

# Mostrar el día, mes y año
print("Día:", dia)
print("Mes:", mes)
print("Año:", año)
