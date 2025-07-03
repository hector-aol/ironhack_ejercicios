# Ejercicio 6. Lectura de archivo
# Se proporciona un archivo de texto llamado datos_usuarios.txt con líneas en el siguiente formato:
# usuario1,25
# usuario2,32
# usuario3,17
# Crea una función que lea el archivo y devuelva un diccionario con usuario como clave y edad (int) como valor.
# Usa manejo de archivos y manejo de strings.

def leer_usuarios(archivo='datos_usuarios.txt'):

    usuarios_edades = {}
    try:
        # Abrir el archivo en modo lectura
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            
        # Procesar cada línea
        for linea in lineas:
            # Eliminar espacios y saltos de línea
            linea_limpia = linea.strip()
            
            # Saltar líneas vacías
            if not linea_limpia:
                continue
                
            # Separar por coma
            partes = linea_limpia.split(',')
            
            # Verificar formato correcto
            if len(partes) < 2:
                continue
                
            # Obtener usuario y edad
            usuario = partes[0].strip()
            edad_str = partes[1].strip()
            
            try:
                # Convertir a entero y guardar
                edad = int(edad_str)
                usuarios_edades[usuario] = edad
            except ValueError:
                print(f"Advertencia: Edad inválida para '{usuario}': '{edad_str}'")
                
        return usuarios_edades
        
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo}' no encontrado")
        return {}
    except Exception as e:
        print(f"Error inesperado: {e}")
        return {}

# Ejemplo de uso
if __name__ == "__main__":
    datos = leer_usuarios()
    print("Diccionario de usuarios:")
    for usuario, edad in datos.items():
        print(f"{usuario}: {edad} años")