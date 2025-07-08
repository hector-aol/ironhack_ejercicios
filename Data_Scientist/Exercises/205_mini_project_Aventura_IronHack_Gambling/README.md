## Mini Proyecto - Aventura de la Base de Datos de IronHack Gambling

[Semana 3](https://my.ironhack.com/cohorts/6791208a1980ce002be29f57/lms/courses/course-v1:IRONHACK+DS_CONSORCI_FT+062025_SOC_DS/modules/ironhack-course-chapter_2)Sesión 15

[Mini Proyecto - Aventura de la Base de Datos de IronHack Gambling](https://my.ironhack.com/cohorts/6791208a1980ce002be29f57/lms/courses/course-v1:IRONHACK+DS_CONSORCI_FT+062025_SOC_DS/modules/ironhack-course-chapter_2/units/ironhack-course-chapter_2-sequential_4-vertical)

## Mini Proyecto - Aventura de la Base de Datos de IronHack Gambling


## Resultados de Aprendizaje

¡Bienvenido a la Aventura de la Base de Datos de IronHack Gambling! Este desafío está inspirado en un escenario de entrevista de trabajo real de IronHack Gambling. Está diseñado para poner a prueba tus habilidades en SQL de una manera divertida y atractiva. Imagina que estás postulando para un puesto de analista de datos en IronHack Gambling, y te han dado este desafío para demostrar tu experiencia. Esta sesión pone a prueba tu dominio de SQL a través de una serie de tareas que van desde la recuperación básica de datos hasta análisis complejos. Utilizando tablas clave de la base de datos como Betting, Product, Customer y Account, abordarás preguntas realistas diseñadas para simular el rol de un analista de datos en GVC Group. Los desafíos incluyen generar listas de clientes, analizar patrones de apuestas y proporcionar ideas accionables para la gestión de marketing y productos. Esta sesión no solo agudiza tus habilidades en consultas SQL, sino que también te prepara para desafíos reales de análisis de datos.

## Proyecto

El resumen del proyecto y el conjunto de datos se pueden encontrar en GitHub:

* **[Mini Proyecto - La Aventura de la Base de Datos de IronHack Gambling](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es)**



[![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Mini Proyecto | La Aventura de la Base de Datos de Apuestas de IronHack

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#mini-proyecto--la-aventura-de-la-base-de-datos-de-apuestas-de-ironhack)

## Introducción

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#introducci%C3%B3n)

¡Bienvenidos a la Aventura de la Base de Datos de Apuestas de IronHack! Este desafío está inspirado en un escenario real de entrevista de trabajo de IronHack Gambling. Está diseñado para poner a prueba tus habilidades en SQL de una manera divertida y atractiva. Imagina que estás aplicando para un rol de analista de datos en IronHack Gambling, y te han dado este desafío para demostrar tu experiencia.

## Escenario

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#escenario)

Se te ha dado acceso a cuatro tablas críticas de la base de datos de IronHack Gambling: `Betting`, `Product`, `Customer` y `Account`. Estas tablas son centrales para el 75% de todas las consultas en IronHack Gambling. Para este desafío, se proporciona una instantánea de datos que involucra a 10 jugadores y sus transacciones. Tu tarea es demostrar tu destreza en SQL recuperando y manipulando estos datos para proporcionar información valiosa.

## Formato del Desafío

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#formato-del-desaf%C3%ADo)

* El desafío comienza con consultas simples y gradualmente aumenta en complejidad.
* Para cada pregunta, escribe tu consulta SQL para encontrar la respuesta.
* Aunque los datos originales están en Excel, concéntrate solo en escribir consultas SQL como si los datos estuvieran en una base de datos SQL.

## Preguntas

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#preguntas)

* **Pregunta 01** : Usando la tabla o pestaña de clientes, por favor escribe una consulta SQL que muestre Título, Nombre y Apellido y Fecha de Nacimiento para cada uno de los clientes. No necesitarás hacer nada en Excel para esta.
* **Pregunta 02** : Usando la tabla o pestaña de clientes, por favor escribe una consulta SQL que muestre el número de clientes en cada grupo de clientes (Bronce, Plata y Oro). Puedo ver visualmente que hay 4 Bronce, 3 Plata y 3 Oro pero si hubiera un millón de clientes ¿cómo lo haría en Excel?
* **Pregunta 03** : El gerente de CRM me ha pedido que proporcione una lista completa de todos los datos para esos clientes en la tabla de clientes pero necesito añadir el código de moneda de cada jugador para que pueda enviar la oferta correcta en la moneda correcta. Nota que el código de moneda no existe en la tabla de clientes sino en la tabla de cuentas. Por favor, escribe el SQL que facilitaría esto. ¿Cómo lo haría en Excel si tuviera un conjunto de datos mucho más grande?
* **Pregunta 04** : Ahora necesito proporcionar a un gerente de producto un informe resumen que muestre, por producto y por día, cuánto dinero se ha apostado en un producto particular. TEN EN CUENTA que las transacciones están almacenadas en la tabla de apuestas y hay un código de producto en esa tabla que se requiere buscar (classid & categoryid) para determinar a qué familia de productos pertenece esto. Por favor, escribe el SQL que proporcionaría el informe. Si imaginas que esto fue un conjunto de datos mucho más grande en Excel, ¿cómo proporcionarías este informe en Excel?
* **Pregunta 05** : Acabas de proporcionar el informe de la pregunta 4 al gerente de producto, ahora él me ha enviado un correo electrónico y quiere que se cambie. ¿Puedes por favor modificar el informe resumen para que solo resuma las transacciones que ocurrieron el 1 de noviembre o después y solo quiere ver transacciones de Sportsbook. Nuevamente, por favor escribe el SQL abajo que hará esto. Si yo estuviera entregando esto vía Excel, ¿cómo lo haría?
* **Pregunta 06** : Como suele suceder, el gerente de producto ha mostrado su nuevo informe a su director y ahora él también quiere una versión diferente de este informe. Esta vez, quiere todos los productos pero divididos por el código de moneda y el grupo de clientes del cliente, en lugar de por día y producto. También le gustaría solo transacciones que ocurrieron después del 1 de diciembre. Por favor, escribe el código SQL que hará esto.
* **Pregunta 07** : Nuestro equipo VIP ha pedido ver un informe de todos los jugadores independientemente de si han hecho algo en el marco de tiempo completo o no. En nuestro ejemplo, es posible que no todos los jugadores hayan estado activos. Por favor, escribe una consulta SQL que muestre a todos los jugadores Título, Nombre y Apellido y un resumen de su cantidad de apuesta para el período completo de noviembre.
* **Pregunta 08** : Nuestros equipos de marketing y CRM quieren medir el número de jugadores que juegan más de un producto. ¿Puedes por favor escribir 2 consultas, una que muestre el número de productos por jugador y otra que muestre jugadores que juegan tanto en Sportsbook como en Vegas?
* **Pregunta 09** : Ahora nuestro equipo de CRM quiere ver a los jugadores que solo juegan un producto, por favor escribe código SQL que muestre a los jugadores que solo juegan en sportsbook, usa bet_amt > 0 como la clave. Muestra cada jugador y la suma de sus apuestas para ambos productos.
* **Pregunta 10** : La última pregunta requiere que calculemos y determinemos el producto favorito de un jugador. Esto se puede determinar por la mayor cantidad de dinero apostado. Por favor, escribe una consulta que muestre el producto favorito de cada jugador

Mirando los datos abstractos en la pestaña "Student_School" en la hoja de cálculo de Excel, por favor responde las siguientes preguntas:

* **Pregunta 11** : Escribe una consulta que devuelva a los 5 mejores estudiantes basándose en el GPA
* **Pregunta 12** : Escribe una consulta que devuelva el número de estudiantes en cada escuela. (¡una escuela debería estar en la salida incluso si no tiene estudiantes!)
* **Pregunta 13** : Escribe una consulta que devuelva los nombres de los 3 estudiantes con el GPA más alto de cada universidad.

## Cómo Participar

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#c%C3%B3mo-participar)

* Escribe o teclea tus respuestas en SQL para cada pregunta en este documento.
* Siéntete libre de usar un editor separado para redactar tus consultas antes de pegarlas aquí.
* Asegúrate de que tus consultas estén bien formateadas y sean fáciles de entender.

## Entrega

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#entrega)

* Una vez que hayas completado el desafío, entrega tus respuestas antes de la siguiente clase.
* Muestra tus habilidades en SQL y experiencia en manipulación de datos.

## ¡Buena suerte!

[](https://github.com/ironhack-labs/mini-project-ih-gambling-db-adventure-es#buena-suerte)

¡Embárcate en esta aventura SQL y muéstranos todo el alcance de tus capacidades de análisis de datos!
