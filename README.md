Intregrantes: 

Edwin Josue Parada Campos  

CODIGO: SMTR043624

Roberto Carlos Chávez Campos  

CODIGO: SMTR044024


Preguntas y respuestas

Enunciado: 

En El Salvador, muchas personas dependen del transporte público para ir a su trabajo, estudio o actividades diarias. Cada día realizan distintos viajes en rutas urbanas o rurales, con tiempos y costos variables. Sin un registro, es difícil saber cuánto se gasta en transporte semanalmente ni cuáles rutas consumen más tiempo o dinero. Se busca un sistema que permita registrar los viajes realizados, y generar una salida en pantalla al final que muestre los datos ordenados de cada viaje realizado. Además, el sistema debe mostrar un resumen con el gasto total semanal y el tiempo total invertido

Preguntas 
• ¿Qué ventajas tiene en comparación con poner todo el código en un solo archivo o utilizar módulos?
Consideramos que la ventaja es que el codigo es mas ordenado y tiene mayor claridad y es que separar el código en clases hace que sea más fácil de entender y mantener, en comparación con tener todo en funciones sueltas o en un solo bloque, por ejemplo si quiero modificar algo o añadirlo se en donde está y puedo guiarme, por eso le pusimos nombres sencillos a cada clase, asi lo entendemos los 2

Añadir que las clases y métodos pueden reutilizarse en otros proyectos o ampliaciones del sistema y si queremos que es sistema crezca lo podemos dividir en varios módulos.

 • ¿Cómo aplicaron la Programación Orientada a Objetos en su solución? Describen el papel de las clases creadas.

Creamos 2 clases principales para que fuera sencillo:

La clase Viaje representa cada viaje realizado, almacenando información como ruta, tipo, costo y tiempo. Encapsula los datos y permite mostrar la información de forma clara

La otra clase es Registro de viaje que administra la colección de viajes, permitiendo agregarlos, mostrarlos ordenados y calcular los totales de gasto y tiempo. Conectar la lógica de gestión de viajes.


 • ¿De qué manera el uso de GitHub facilitó el trabajo colaborativo en equipo? Den un ejemplo concreto.

Consideramos que un tener un repositorio de github nos ayuda a agilizar el tiempo y trabajar mejor con la parte de el código, al ver los cambios y al poder modificarlos nos facilita el trabajo un montón. Un ejemplo que podríamos dar es que un miembro pudo trabajar en la clase Viaje mientras otro desarrollaba la clase RegistroViajes. Luego, ambos cambios se integraron fácilmente usando la opción que aparece en vs code  pull requests y  se puede revisar quién hizo cada cambio y arreglar errores si es necesario.
