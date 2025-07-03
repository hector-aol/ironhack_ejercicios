# EJERCICIO 19
# Escribir un programa que pregunte el correo electronico del usuario en la consola y muestre
# por pantalla otro correo electronico con el mismo nombre (la parte delate de la arroba '@') 
# pero con dominio ceu.es

correo_usuario = input('Cual es tu correo electronico?: ')
correo_partes = correo_usuario.split('@')
nombre_usuario = correo_partes[0] #Parte 0 = nombre de usuario, Parte 1 = dominio del correo.
nuevo_correo_usuario = nombre_usuario + "@ceu.es"
print("Tu nuevo correo es: ",nuevo_correo_usuario)



