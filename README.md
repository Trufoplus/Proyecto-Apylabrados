# Apylabrados
![Top Language](https://img.shields.io/github/languages/top/Trufoplus/Proyecto-Apylabrados?style=for-the-badge&color=%2300AABB) ![Forks](https://img.shields.io/github/forks/Trufoplus/Proyecto-Apylabrados?style=for-the-badge&color=%23AA0067) ![Stars](https://img.shields.io/github/stars/Trufoplus/Proyecto-Apylabrados?style=for-the-badge&color=%23ffff00) 
### Acerca de Apylabrados
Apylabrados es un juego de palabras similar al apalabrados creado con Python.
### Por que Apylabrados
Este es un proyecto pensado para practicar todo lo aprendido en el curso de Python. 

# Guia de Apylabrados: el juego de palabras

## Objetivos

Implementar un programa que permita al usuario jugar de forma individual al juego de palabras conocido como Apylabrados.

## Normas del juego

* En este juego sólo juega un jugador. El objetivo es conseguir poner el número máximo de puntos.
* El tablero de juego consta de 15 filas por 15 columnas.
* El tablero tiene un total de 225 casillas que pueden contener una letra o estar vacías. Al empezar el juego, el tablero debe estar vacío.
* La casilla central del tablero es especial, pues es la casilla donde debe situarse la primera palabra. Es decir, al menos una de las fichas que conformen la primera palabra debe situarse en la casilla central.
* Se dispone de las siguientes fichas:
````
| Ficha | Total | | Ficha | Total | | Ficha | Total | 
| :---: | :---: | | :---: | :---: | | :---: | :---: | 
| A     | 12    | | J     | 1     | | S     | 7     | 
| B     | 2     | | K     | 1     | | T     | 4     | 
| C     | 4     | | L     | 4     | | U     | 6     | 
| D     | 5     | | M     | 3     | | V     | 1     | 
| E     | 12    | | N     | 5     | | W     | 1     | 
| F     | 2     | | O     | 9     | | X     | 1     | 
| G     | 2     | | P     | 2     | | Y     | 1     | 
| H     | 2     | | Q     | 1     | | Z     | 1     | 
| I     | 6     | | R     | 5     | |       |       | 
````

* Cada ficha tiene la siguiente puntuación: 

````
| Ficha | Puntuación | | Ficha | Puntuación | | Ficha | Puntuación | 
| :---: | :--------: | | :---: | :--------: | | :---: | :--------: | 
| A     | 1          | | J     | 8          | | S     | 1          | 
| B     | 3          | | K     | 5          | | T     | 1          | 
| C     | 3          | | L     | 1          | | U     | 1          | 
| D     | 2          | | M     | 3          | | V     | 4          |   
| E     | 1          | | N     | 1          | | W     | 4          | 
| F     | 4          | | O     | 1          | | X     | 8          | 
| G     | 2          | | P     | 3          | | Y     | 4          | 
| H     | 4          | | Q     | 10         | | Z     | 10         | 
| I     | 1          | | R     | 1          | |       |            | 
````


* Cuando empieza el juego, se deben seleccionar 7 fichas de manera aleatoria, teniendo en cuenta que el total de fichas es 100.
* En cada turno, se debe mostrar al usuario las fichas de las que dispone para poder formar una nueva palabra y colocarla en el tablero. Como se dijo anteriormente, la primera palabra debe tener al menos una ficha sobre la casilla central.
* Para poder colocar una palabra nueva en el tablero, el usuario deberá indicar la fila y la columna donde colorcar la primera ficha de la palabra y la dirección (vertical u horizontal) en la que se colocará la palabra. La casilla superior izquierda es la casilla (0, 0); la casilla inferior derecha es la (14, 14); la casilla central es la casilla (7, 7).
* El programa debe verificar que la palabra puede situarse en el tablero. La verificación consiste en:
  - Comprobar que la palabra exite, mediante su búsqueda en un diccionario (será un fichero de texto).
  - Validar que la palabra cabe en el tablero sin superar los márgenes.
  - Comprobar que la nueva palabra añade al menos una nueva ficha al tablero.
  - Validar que la nueva palabra no sobreescribe fichas ya existentes sobre el tablero.
  - Comprobar que se usa al menos una ficha de las ya existentes sobre el tablero. Si se trata de la primera palabra, validar que pasa por la casilla central.
  - Validar que se puede formar la palabra en cuestión con las fichas del jugador y las que ya se encuentran sobre el tablero
* Tras cada palabra colocada, se deben proporcionar nuevas fichas al jugador, tantas como haya utilizado para que vuelva a tener un total de 7 fichas disponibles.
* Tras cada palabra colocada, se debe mostrar la puntuación del jugador. Añadir tras cada jugada la puntuación de las nuevas fichas colocadas sobre el tablero a la puntuación del jugador.
* El usuario puede solicitar la información sobre la puntuación de cada ficha.
* El usuario puede solicitar ayuda al programa para comprobar si exite alguna colocación para la palabra dada. El programa devolverá todas las posibles posiciones para dicha palabra sobre el tablero, teniendo en cuenta la configuración en la que se encuentre.
* El usuario puede solicitar ayuda al programa para comprobar si puede formar alguna palabra con las fichas de las cuales dispone. El programa devolverá todas las posibles palabras que se puedan formar con las 7 letras del jugador y las letras que haya sobre el tablero haciendo uso del diccionario.
  

## Información adicional

* El diccionario de palabras es un fichero de texto que contiene todas las palabras que se pueden formar. Cada palabra se encuentra en una línea del fichero. Las palabras están en mayúsculas.
* Si la palabra no se encuentra en el diccionario, entonces dicha palabra no es válida y no puede situarse sobre el tablero.
* Se proporcionará un fichero de ejemplo, pero es posible utilizar cualquier otro diccionario que se considere.
