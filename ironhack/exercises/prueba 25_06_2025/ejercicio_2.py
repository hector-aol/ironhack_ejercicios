# Ejercicio 2. Manejo de cadenas
# Pide al usuario una cadena por consola, y:
# Convierte todo a minúsculas.
# Elimina espacios al principio y al final.
# Devuelve una lista con las palabras que tienen más de 3 letras, ordenadas alfabéticamente.


    # Paso 1: Pedir cadena al usuario
entrada = input("Introduce una cadena de texto: ")
    
    # Paso 2: Convertir a minúsculas
cadena_min = entrada.lower()
    
    # Paso 3: Eliminar espacios al principio y final
cadena_limpia = cadena_min.strip()
    
    # Paso 4: Dividir en palabras
palabras = cadena_limpia.split()
    
    # Paso 5: Filtrar palabras con más de 3 letras
palabras_filtradas = [palabra for palabra in palabras if len(palabra) > 3]
    
    # Paso 6: Ordenar alfabéticamente
palabras_filtradas.sort()
    

print("Palabras resultantes:", palabras_filtradas)