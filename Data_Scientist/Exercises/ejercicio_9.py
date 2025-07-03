# EJERCICIO 9 
# Ha fallado el redondeo
cantidad_inversion = float(input('Dime la cantidad a invertir: '))
interes_anual =  float(input('Dime el interes anual: '))
años_inversion = int(input('Dime el numero de años a invertir: '))
capital_obtenido = cantidad_inversion * (1 + interes_anual/100) ** años_inversion
capital_obtenido_rounded = float(round(capital_obtenido, 2))
print('El capital obtenido es: ', capital_obtenido)
