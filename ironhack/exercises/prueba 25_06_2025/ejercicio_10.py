from functools import reduce

# --- Función para leer usuarios desde archivo ---
def leer_usuarios(archivo='datos_usuarios.txt'):
    try:
        with open(archivo, 'r') as f:
            return {
                partes[0].strip(): int(partes[1].strip())
                for linea in f
                if (partes := linea.strip().split(',')) and len(partes) >= 2
            }
    except Exception as e:
        print(f"Error leyendo el archivo: {e}")
        return {}

# --- Función para filtrar usuarios por edad mínima ---
def filtrar_usuarios(usuarios_dict, **kwargs):
    edad_minima = kwargs.get('edad_minima', 18)
    return [
        {'usuario': u, 'edad': e}
        for u, e in usuarios_dict.items()
        if e >= edad_minima
    ]

# --- Función para calcular promedio y marcar mayores que el promedio ---
def calcular_promedio_y_etiquetar(lista_usuarios):
    if not lista_usuarios:
        return []

    suma_edades = reduce(lambda acc, u: acc + u['edad'], lista_usuarios, 0)
    promedio = suma_edades / len(lista_usuarios)

    for usuario in lista_usuarios:
        usuario['mayor_que_promedio'] = usuario['edad'] > promedio

    return lista_usuarios

# --- Función para generar informe a archivo ---
def generar_informe(lista_usuarios, archivo_salida='informe_usuarios.txt'):
    if not lista_usuarios:
        print("No hay datos para generar el informe")
        return

    try:
        with open(archivo_salida, 'w') as f:
            for usuario in lista_usuarios:
                linea = (f"{usuario['usuario']} tiene {usuario['edad']} años - "
                         f"Mayor que promedio: {usuario['mayor_que_promedio']}\n")
                f.write(linea)
        print("Informe generado exitosamente!")
    except Exception as e:
        print(f"Error al escribir el informe: {e}")

# --- Función principal que integra todo el proceso ---
def procesar_usuarios(archivo_entrada='datos_usuarios.txt', archivo_salida='informe_usuarios.txt', **kwargs):
    usuarios_dict = leer_usuarios(archivo_entrada)
    lista_filtrada = filtrar_usuarios(usuarios_dict, **kwargs)
    lista_etiquetada = calcular_promedio_y_etiquetar(lista_filtrada)
    generar_informe(lista_etiquetada, archivo_salida)

# --- Ejemplo de uso ---
# Se puede cambiar edad mínima u otros filtros así:
procesar_usuarios(edad_minima=21)
