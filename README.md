# Algortimos de recursion
El proposito de este proyecto es entender el funcionamiento de los algoritmos recursivos.
Tambien estudiar sus formas iterativas, que tan rentable sale usarlas en comparacion de las recursivas.
-- todos estos algoritmos son programados en python -- 
Algortimos principales:
1. Sumar los digitos de un numero:
   Se divide el numero por 10 y obtenemos tambien su modulo en 10, asi las veces que sean necesarias hasta cubrir todos los digitos del numero.
3. Invertir cadena:
   Se selecciona el ultimo caracter de la cadena y se inserta en una nueva, asi hasta que ya no quede un caracter.
5. Busqueda binaria:
  Partiendo de un conjunto de datos ya ordenado, este se divide en dos partes iguales. Se toma el valor central como punto de referencia y se compara con el elemento que buscamos. Si nuestro elemento es mayor que el central,   se descarta la mitad izquierda y el proceso se repite únicamente en la mitad derecha.
7. potenciacion:
   Descompone un problema grande (como $2^3$) en una versión más pequeña de sí mismo (2 * 2^2). Este proceso se repite hasta llegar al caso base, que es cuando la potencia es 0 ($a^0$), momento en el que la función devuelve     1.
