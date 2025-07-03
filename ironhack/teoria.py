# TIPOS DATOS --> type(<<variable>>) --> str | int - float | bool | [] - () - {}
# OPERACIONES INT FLOAT --> * + - / ** // %
# OPERACIONES STR --> concatenar | replicar 
# OPERACIONES LOGICAS CON DATOS --> extrictos (> <) - igualdad ( == | is) - superioridad/inferioridad ( >= <= ) - distinto ( != )
# METODOS DE STR --> Manipulacion (upper,lower,title,capitalize,swapcase) | Comprobacion (isalpha,isdigit,isalnum,islower,isupper,isspace,istitle)
#                    modificacion y remplazo(replace,strip,r/l/strip,join,split,zfill,expandtabs) | alineacion (center,l/r/just)
#                    busqueda (find , rfind , index , rindex , count , startwith | endswith)
# SLICING STR --> [<<Ind_ini>> : <<Ind_fin>> : <<paso>> ] [:-:]
# BUCLES
#     for <<cursor>> in <<estructura_datos>>:
#       <<operacion_por_bucle>>
#
#     while <<cond>>:
#       <<operacion_por_bucle>>
#       <<actualizacion_cursor>>
# PRINT(<<variable> , sep = " ")
# FORMATEO DE STRING:   f"...{}" | f"...%s...%d"$(<<valor1>,<<valor2>) | f"...{}...{}".format(<<valor1>,<<valor2>) | f"...{clave}...".format_map({<<clave>:<<valor>})
# FUNCIÓN : paquetiza codigo y puede ser de dos tipos: declarativas y no declarativas 
#  a) declarativa
#   def <<nombre_funcion>>(<<parámetros>>):
#       <<cuerpo_funcion>>
#       return <<elemento/s_a_devolver>>
#   Parámetros:
#     - predefinidios: (<<parametro/s>> = <<valor>> , ... , <<parametro/s>> = <<valor>>)
#     - variables:     (*<<parametro/s>>)
#     - clave-valor:     (**<<parametro/s>>)
#   Tipos de funcion declarativa:
#     - Funcion anidada -> funcion que contiene funciones y la funcion principal instancia al a subfunción como parámetro
#          def calculadora(a=0,b=0,c="sumar"):
#              def sumar(a,b):
#                  return a+b
#              def restar(a,b):
#                  return a-b
#              if c == 'summar':
#                  return sumar(a,b)
#              else:
#                  return restar(a,b)
#     - Funcion clousure -> subfunción instanciada desde la funcion principal -> funcion_ppal(<<parámetros>>)()
#          def ope(a , b):
#              def sumar(a,b):
#                  return a+b  
#              return sumar
#     - Funcion decoradora -> funcion principal que se ejecuta hasta un punto donde se ejecuta una funcion externa y continua la ejecución de la función ppal
#          def <<fun_ppal>>(<<funcion_externa>>):
#              <<primera_parte_a_ejecutar_del_cuerpo_de_la_funcion_ppal>>
#              funcion_externa()
#              <<segunda_parte_a_ejecutar_del_cuerpo_de_la_funcion_ppal>>
#          @fun_ppal
#          def <<funcion_externa>>(<<parámetros>>):
#              <<cuerpo_funcion>>
#              return <<elemento/s_a_devolver>>
#     - Funcion generadoras -> funciones que son consumidas por petición 
#          def <<funcion_generadora>>(<<parámetros>>):
#              <<cuerpo_funcion_consumido_en_la_primera_llamada>>
#              yield 
#              .
#              .
#              .
#              <<cuerpo_funcion_consumido_en_la_N_llamada>>
#              yield 
#          next(funcion_generadora)       
#  b) no declarativa u anonima
#   <<varible>> = lambda <<parámetros>> : <<return_como_cuerpo_de_funcion>>
#   <<varible>> = lambda <<parámetros>> : <<return_como_cuerpo_de_funcion>> <<condicion>> --> ej  lambda x : x**2 if x%2 == 0 else x**3
# VARIABLES : en python hay dos tipos de variables
#   - Global : variable que esta al nivel de ejecución del script principal, y afecta a todos los niveles de subejecución -> globals()
#   - Local  : variables efimeras que surgen a nivel de  subejecución (pej. en la creación de variables de variables intermedias de una función) y no se extienden a la ejecución ppal -> locals()
#   Hay una libreria: "import inspect" que hace una fotografia de variables con 'frame = inspect.currentframe()' y obter las:
#    a) globales con: frame.f_globals
#    b) locales con:  frame.f_locals
#   Se puede extender una variable local a global con el método: 'global'
# LISAS : [] , list() --> indices que van de 0 a len(<<lista>>)-1
#   - Se puede usar slicing en ellas
#   - Metodos: append(<<un_dato>>) , insert(<<indice>>,<<un_dato>>) ,  extend(<<lista>>) , remove(<<un_dato>>) , pop(<<indice>>) , clear() , 
#              index( <<un_dato>> ) , count( <<un_dato>> ) , sort(reverse=False/True) , reverse() , copy()
#   - Tipos: 
#       a) Extensionales: Los que se crean mediante la definición de las listas con sus valores, o el resultado de añadirlos con metodos
#       b) Intensional o de compresion
#             - [<<elemento_comun>> <<for_in_sequence>> <<condicion_if>>]
#             - [<<operacion1_ec>> if <<condicion>>  else <<operacion2_ec>> <<for_in_sequence>>] 
#             - [<<operacion1_ec>> if <<condicion1>>  else <<operacion2_ec>> if <<condicion2>> else <<operacion3_ec>>  <<for_in_sequence>>] 
# ITERADORES: 
#    - iter(<<lista>>) + next(<<var_del_iter>>)
#    - enumerate(<<lista>>) --> ej for i, j in enumare([7,3,8]) 
#    - zip(<<lista1>> , <<lista1>>)  
#    - map (<<funcion>> , <<lista>>) 
#    - filter (<<funcion_filtrado>> , <<lista>>) 
# DICCIONARIOS: dict() , {<<clave>> : <<valor>>}
#    - Metodos: get(<<clave>>) , keys() , values() , items() , update(<<diccionario>>) , pop(<<clave>>) , clear() , copy()
#    - Tipos:
#       a) Extensionales: Los que se crean mediante la definición del diccionario con sus valores, o el resultado de añadirlos con metodos
#       b) Intensional o de compresion
#             - {<<clave>> : <<operacion_ec>> <<for_in_sequence>> <<condicion_if>>}
#             - {<<clave>> : <<operacion1_ec>> if <<condicion>>  else <<clave>> : <<operacion2_ec>> <<for_in_sequence>>} 
#             - {<<clave>> : <<operacion1_ec>> if <<condicion1>>  else <<clave>> : <<operacion2_ec>> if <<condicion2>> else <<clave>> : <<operacion3_ec>>  <<for_in_sequence>>} 
# ERRORES: 
#    try:
#        <<operacion_que_puede_dar_error>>
#    except <<clave>>:
#        <<operacion_tipo_de_error_especifico>>
#    else:
#        <<operacion_si_el_error_no_esta_contemplado>>
#    finally:
#        <<continuacion_codigo_ocurra_o_no_error>>
#    - Tipos de errores:
#         * SyntaxError -> no respetamos la sintaxis de python
#         * IdentationError -> errores resultado de falta de identacion
#         * NameError -> llamamos a una variable q no está definida
#         * TypeError -> Un tipo de dato es incorrecto en una operacion
#         * ValueError -> casteos con problemas
#         * IndexError -> el indice no existe
#         * KeyError -> La clave no existe
#         * AtributeError -> uso de un atributo o metodo que no existe
#         * ZeroDivisionError -> indeterminacion de division por cero
#         * FileNotFoundError -> archivo no encontrado
#         * ImportError -> No se puede importar el modulo
#         * RuntimeError -> error generico durante la ejecución
# LIBRERIA DIRECTORIOS/ARCHIVOS
#  a) OS: import os
#    - Metodos:
#         * os.getcwd() ->  directorio actual de ejecucion
#         * os.chdir(<<ruta>>) -> cambiar el direcorio de trabajo a la ruta
#         * os.listdir(<<ruta>>) -> listar carpetas en una ruta
#         * os.mkdir(<<nombre_carpeta>>) -> crea carpeta en la ruta en la que os encontrais 
#         * os.mkdirs(<<ruta>>) -> crea carpetas anidadas
#         * os.remove(<<ruta>>) -> elimina un archivo
#         * os.rmdir(<<carpeta>>) -> elimina carpeta vacia
#         * os.removedirs(<<ruta>>) -> elimina carpetas anidadas vacías
#         * os.rename(<<nombre_archivo_old>>,<<nombre_archivo_new>>) -> renombra un archivo
#         * os.path.exists(<<archivo>>) -> Devuelve True si existe el archivo
#         * os.path.isfile(<<archivo>>) -> Devuelve True si es un archivo
#         * os.path.isdir(<<archivo>>) -> Devuelve True si es un directorio
#         * os.path.join(<<ruta>>,<<archivo>>) -> Devuelve una ruta con el archivo en formato direccion URI
#         * os.path.basename(<<ruta>>) -> Devuelve de la ruta el nombre del directorio o carpeta
#         * os.path.dirname(<<ruta>>) -> Devuelve de la ruta el nombre del directorio base
#         * os.path.split(<<ruta>>) -> separa en directorio y archivo
#         * os.path.splitext(<<archivo>>) -> separa del archivo su nombre y su extension
#  b) SHUTIL: import shutil
#    - Metodos:
#         * shutil.rmtree() -> borrar un directorio esté o no vacio
#         * shutil.move(<<archivo>>,<<ruta>>) -> mover un archivo a un directorio 
# APERTURA DE ARCHIVOS: open() o with open()
#    - Modos:
#         * r -> lectura
#         * w -> escritura
#         * a -> añadir al final
#         * x -> creacion
#    - Metodos:
#         * write(<<dato>>) -> borra si existe/crea sino existe y escribe
#         * read(<<n>>) -> lee todo el archivo o hasta n lineas
#         * readline() -> lee una linea
#         * close() -> cerrar el método open [exclusivo de open()]
#    - Sintaxis:
#        a) <<variable>> = open(<<archivo>> , <<modo>> , encoding = <<coding>>)
#           <<variable>>.close()
#        b) with open(<<archivo>> , <<modo>> , encoding = <<coding>>) as <<variable>>
#               <<cuerpo_sintaxis>>