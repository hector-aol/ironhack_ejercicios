# EJERCICIOS 11
dinero_depositado = float(input('Cual es la cantidad de dinero depositado?:' ))
interes_anual = 4
dinero_obtenido_primer_año = dinero_depositado * (1+interes_anual/100)
dinero_obtenido_segundo_año = dinero_obtenido_primer_año * (1+interes_anual/100)
dinero_obtenido_tercer_año = dinero_obtenido_segundo_año * (1+interes_anual/100)
print('El dinero obtenido el primer año es:', round(dinero_obtenido_primer_año, 2))
print('El dinero obtenido el segundo año es:', round(dinero_obtenido_segundo_año, 2))
print('El dinero obtenido el tercer año es:', round(dinero_obtenido_tercer_año, 2))

