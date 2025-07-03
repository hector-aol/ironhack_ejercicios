# Ejercicio 1. Conteo condicional
# Escribe una función que reciba una lista de números enteros y retorne cuántos números:
# Son positivos
# Son negativos
# Son pares
# Son impares
# Usa bucles for, condicionales if-else, y devuelve un diccionario con los conteos.
# Se pide confeccionar los flujogramas.

def contar_numeros(lista):
    positivos, negativos, pares, impares = 0, 0, 0, 0

# Contar positivos y negativos
    for numero in lista:  
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        
# Contar pares e impares
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    return {
        'positivos': positivos,
        'negativos': negativos,
        'pares': pares,
        'impares': impares
    }

# Ejemplo de uso
resultado = contar_numeros([1, -2, 0, 5, 7, -3, 4])
print(resultado)  # {'positivos': 3, 'negativos': 2, 'pares': 3, 'impares': 4}
