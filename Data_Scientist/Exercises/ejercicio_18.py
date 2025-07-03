# # EJERCICIO 18
# # Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
# # y despues muestre por pantalla la misma frase pero con la vocal introducida en mayuscula.

# frase = input("Introduce una frase: ")
# vocal = input("Introduce una vocal: ")

# # Convertimos la vocal a minúscula para identificar todas sus ocurrencias
# vocal_minuscula = vocal.lower()

# # Reemplazamos todas las ocurrencias de la vocal (en minúscula) por su versión en mayúscula
# frase_modificada = frase.replace(vocal_minuscula, vocal.upper())

# print(f"Frase modificada: {frase_modificada}")

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal: ")

vocal_minuscula = vocal.lower()
vocal_mayuscula = vocal.upper()

longitud_vocal = len(vocal_minuscula)
nueva_frase = ""
i = 0

while i < len(frase):
    # Verificar si la subcadena actual coincide con vocal_minuscula
    if longitud_vocal > 0 and i + longitud_vocal <= len(frase):
        if frase[i:i+longitud_vocal] == vocal_minuscula:
            nueva_frase += vocal_mayuscula
            i += longitud_vocal
            continue
    # Si no coincide, agregar el carácter actual
    nueva_frase += frase[i]
    i += 1

print(f"Frase modificada: {nueva_frase}")

