# EJERCICIO 7
# Formula para obtener el indice de masa corporal IMC = peso / (altura ** 2)
peso_kg = float(input('Dime tu peso en kilogramos: '))
estatura = float(input('Dime tu estatura exacta en metros: '))
indice_masa_corporal = peso_kg / (estatura ** 2)
indice_masa_corporal_dos_decimales = float(round(indice_masa_corporal, 2))
print('\nTu indice de masa corporal es: ',indice_masa_corporal_dos_decimales)

