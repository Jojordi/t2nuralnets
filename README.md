**Problema Escogido**

Para la implementación de la tarea se escogió el problema del laberinto.

***Gen***

Se considera como gen un solo intento de movimiento hacia alguna celda aledaña. Dicho movimiento
puede ser fructuoso o infructuoso.

***Individuo***

Se considera como individuo un arreglo de tamaño igual a la cantidad de celdas presentes en el laberinto, pues en caso 
ideal
se necesitan menos movimientos que eso para llegar al final del laberinto.

***Funcion de Fitness***

Se consideraron diversas iteraciones de funciones de fitness para este problema:
 <li> Considerar la celda actual como el puntaje: Debido a como esta planteado el problema se sabe que se parte en la 
 celda numero 0 y se termina en la celda con numero igual a la cantidad de celdas - 1. El problema es que se reportaría
 como positivo solo el avanzar en celdas y no necesariamente llegar al final por lo cual se descartó la función.
 <li> Considerar moverse a la derecha y hacia abajo como progreso y movimientos a la izquierda y arriba como retroceso:
 Dado dado que la solución óptima baja y va a la derecha más que subir e ir a la izquierda se utilizó esta iteración. El
 problema es cuando se necesita hacer la clase de movimientos que restan puntaje.

La función de fitness final considerara es una que contabiliza la cantidad de veces que una celda fue visitada y además 
remueve puntaje a los individuos que choquen con uno de los lados. Sin embargo la implementación posee bugs y no se 
encuentra óptimamente funcional.


**Implementación**


Se considera que el algoritmo genético es lo suficientemente general como para hacerlo una clase aparte que utilize
las funcionalidades de clases adicionales para poder resolver problemas específicos.

La clase del algoritmo genético entonces realiza las funciones de aquel utilizando los métodos, variables, 
especificaciones y funcionalidades de la clase provista. En este sentido toda especialización del problema debe ser 
provista por una clase que provea las funciones que requiere el algoritmo genético adaptadas al problema a resolver.

En base a los gráficos obtenidos y observados se aprecia el carácter logarítmico de la evolución de los individuos 
mientras se acercan al resultado deseado


