#Escribir un programa que pregunte el nombre completo del usuario en la consola y despues
#muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras
#minusculas, otra con todas las letras mayusculas y otra sola con la primera letra del nombre
#y de los apellidos en mayusculas. El usuario puede introducir su nombre combinando mayusculas
#y minisculas como quiera.

nombre_completo_usuario = input('Introduce tu nombre completo de usuario: ')
minus = nombre_completo_usuario.lower()
mayus = nombre_completo_usuario.upper()
title_formato_nombre = nombre_completo_usuario.title()

print(minus)
print(mayus)
print(title_formato_nombre)