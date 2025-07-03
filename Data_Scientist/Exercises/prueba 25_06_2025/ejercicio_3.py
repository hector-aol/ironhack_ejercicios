# Ejercicio 3. Función recursiva + valores predefinidos
# Define una función recursiva que calcule la suma de los dígitos de un número entero positivo. 
# Usa un parámetro adicional con valor por defecto que acumule la suma. No utilices str() para 
# convertir el número.

def suma_digitos(n, acum=0):
   
# Caso base: cuando no quedan dígitos
    if n == 0:
        return acum
    
 # Paso recursivo: obtener último dígito y reducir el número
    ultimo_digito = n % 10
    nuevo_n = n // 10
    nuevo_acum = acum + ultimo_digito
    
    return suma_digitos(nuevo_n, nuevo_acum)


if __name__ == "__main__":
    print(suma_digitos(1234))  
    print(suma_digitos(1000))   
    print(suma_digitos(999))    
    print(suma_digitos(5))      