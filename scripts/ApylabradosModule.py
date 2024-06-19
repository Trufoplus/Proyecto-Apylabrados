import csv
import random
import numpy as np
import itertools
import matplotlib.pyplot as plt


###############################################################################
### TRABAJO CON LAS FICHAS
###############################################################################
class Pawns():
    #Valor en puntos de cada letra
    points = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 
        'H': 4, 'I': 1, 'J': 8, 'K': 5, 'L': 1, 'M': 3, 'N': 1, 
        'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 
        'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }
    
    def __init__(self, letters: str = None):
        """
        Crear la bolsa de fichas (pawns) del juego.

        Args:
            letters (list, optional): Bolsa con las fichas/letras por defecto
            estará vacia.
        """
        self.letters = letters
        if letters is None:
            self.letters = []
        else:
            self.letters = letters.copy()
    
    def addPawn(self, c: str):
        """
        Añade una pieza(pawn) al conjunto de letras

        Args:
            c (str): letra a añadir
        """
        self.letters.append(c)
    
    def addPawns(self, c: str, n: int):
        """
        Añadir Varias fichas a la vez de la misma letra

        Args:
            c (str): Letra de la ficha
            n (int): Numero de fichas a añadir
        """
        for time in range(n):
            self.addPawn(c)
    
    def createBag(self):
        """
        Crea la bolsa de fichas inicial a partir de archivo
            bag_of_pawns.csv
        """
        bags_of_pawns = r"D:\Programacion\Git_And_GitHub\Proyecto-python-fin-curso\datas\bag_of_pawns.csv"
        with open(bags_of_pawns, "r") as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if isinstance(row[1], float):
                    self.addPawns(row[0], int(row[1]))
    
    def showPawns(self):
        """
        Muestra el numero de fichas que hay en la bolsa
        """
        total_pawns = len(self.letters)
        if total_pawns > 0:
            return self.getFrecuency()
        else:
            print("La bolsa de fichas esta vacia")
            return {}
    
    def takeRandomPawn(self):
        """
        Agarra una ficha aleatoria de la bolsa y la elimina de la bolsa.
        """
        if self.letters:
            random_pawn_index = random.randint(0, len(self.letters) -1)
            my_pawn = self.letters.pop(random_pawn_index)
            return my_pawn
        else:
            print("La bolsa de fichas esta vacia, no puede agarrar mas")
    
    def getFrecuency(self):
        """
        Calcula y devuelve la frecuencia de cada ficha en la bolsa.
        """
        frequency_pawns = FrecuencyTable()
        for letter in self.letters:
            frequency_pawns.update(letter)
        return frequency_pawns.showFrequency()       

    def takePawn(self, c:str):
        """
        Recibe del cojunto de fichas de jugador la ficha que ya esta en el 
        tablero y la devuelve a la mano
        
        Args:
            c (str): ficha del jugador
        """
        self.c = c
        self.addPawn(c)
    
    @staticmethod
    def getTotalPawns(word):
        """
        Devuelve el numero de ficha que tiene la palabra introducida por el
        jugador
        
        Args:
            word (obj): objeto de la clase word
            
        Returns:
            str list: lista de letras
        """
        return [letter for letter in word.word[0]]
    
    @staticmethod
    def getPoints(c:str):
        """
        Obtiene la puntuacion de la letra introducida.

        Args:
            c (str): Una letra cualquiera

        Returns:
            int : Devuelve el valor en puntos de la letras
        """
        return Pawns.points[c]
    
    @staticmethod
    def showPawnsPoints():
        """
        Muestra el valor en puntos de cada letra
        """
        print("\nPuntuación de las letras:")
        print("-" * 40)
        for letter, point in Pawns.points.items():
            print(f"{letter} -> {point} puntos")
        


###############################################################################
### LOGICA DE LAS PALABRAS
###############################################################################
class Word():
    def __init__(self):
        self.word = []
    
    def __str__(self):
        """
        Imprimimos la palabra en formato string
        """
        return ', '.join(self.word)
    
    def areEqual(self, w:str):
        """
        Comprueba si dos palabras son iguales
        """
        return w in self.word
    
    def isEmpty(self):
        """
        Comprueba si una palabra esta vacia
        """
        return not self.word
    
    @classmethod
    def readWord(cls):
        """
        Lee una palabra por teclado y la devuelve como un objeto de la clase Word
        """
        input_word = input("Escribe una palabra con tus fichas").strip().upper()
        w = Word()
        w.word.append(input_word)
        return w
    
    @staticmethod
    def readWordFromFile(f):
        """
        lee una palabra de un fichero
        """
        return f.readline().strip().upper()    

    def getFrecuency(self):
        """
        Devuelve el numero de letras que contiene la palabra introducida
        """
        frequency = FrecuencyTable()
        for letter in self.word[0]:
            frequency.update(letter) #Agrega la letra a la tabla de frecuencias de letras.
        return frequency.showFrequency() #Letras con mas de una frecuencia en la tabla de frecuencias.              


###############################################################################
### DICCIONARIO PALABRAS EMPLEADAS EN EL JUEGO
###############################################################################    
class Dictionary():
    dictionary = r"D:\Programacion\Git_And_GitHub\Proyecto-python-fin-curso\datas\word_list.txt"
    
    @staticmethod
    def validateWord(word:str):
        """
        Comprueba si una palabra esta en el diccionario
        """
        with open(Dictionary.dictionary, 'r', encoding='utf-8') as file:
            while True:
                readed_line = Word.readWordFromFile(file)
                if word.areEqual(readed_line):
                    return True
                if readed_line == "":
                    return False
    
    @staticmethod
    def showWord(pawns):
        """
        Genera las posibles combinaciones de palabras con las fichas recibidas
        
        """
        letters = pawns.letters
        combinations = []
        
        #genera todas las posibles combinaciones y las guarda en una lista
        for i in range(1, len(letters) + 1):
            combinations.extend([''.join(p) for p in itertools.permutations(letters, i)])

        # Carga el listado de palabras españolas
        with open(Dictionary.dictionary, "r", encoding="utf-8") as f:
            words = [line.strip().upper() for line in f]
   
        #Muestra las combinaciones si esta no esta en el diccionario
        word_list = []
        for combination in combinations:
            if combination in words and len(combination) > 2:
                if combination not in word_list:
                    word_list.append(combination)

        #Muestra las palabras
        if word_list:
            for word in word_list:
                print(word)
        else:
            print("\nNo se han encontrado combinaciones con tus letras")
            print("Se te repartiran nuevas fichas\n")
            return False          

    @staticmethod
    def showWordPlus(pawns, c:str):
        """
        Recibe un objeto pawns de la clase Pawns y un caracter c y muestra todas 
        las posibles palabras que contienen el caracter c y que se pueden formar 
        las fichas de pawns.

        Args:
            pawns: listado de fichas/letras disponibles
            c : un caracter
        """
        letters = pawns.letters
        c = c.upper()
        
        #agrega la letra a la lista si no se encuentra en ella
        if c not in letters:
            letters.append(c)
        
        # Carga un listado de palabras españolas
        with open(Dictionary.dictionary, "r", encoding="utf-8") as f:
            words = [line.strip().upper() for line in f]
            
        #Realiza todas las posibles combinaciones
        word_list = []
        for i in range(1, len(letters) + 1):
            for combination in itertools.permutations(letters, i):
                word = ''.join(combination)
                # Verificar que la palabra contiene el carácter c y es válida
                if c in word and word in words and len(word) > 2:
                    if word not in word_list:
                        word_list.append(word)        
        
        #Muestra las palabras
        for word in word_list:
            print(word)          

###############################################################################
### TABLA DE FRECUENCIAS DE FICHAS
###############################################################################
class FrecuencyTable():
    def __init__(self):
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                        'n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.frequencies = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
       
    def showFrequency(self):
        """
        Muestra el numero de veces que aparece una letra

        Returns:
            set : letras en el conjunto
        """
        letters = []
        for letter, frequency in zip(self.letters, self.frequencies):
            if frequency != 0:
                print(f'{letter.upper()}: {frequency}')
                letters.append(letter)           
        return letters
    
    @staticmethod
    def isSubset(letters_1, letters_2):
        """
        Verifica si las letras del conjunto 1 estan en el conjunto 2

        Args:
            letters_1 : Conjunto de letras 1
            letters_2 : Conjunto de letras 2

        Returns:
            bolean : False o True si se cumple la condicion
        """
        temp_letters_2 = letters_2.copy()
        for letter in letters_1:
            # nos aseguramos que la letra esta en mayuscula para hacer la verificacion.
            letter  = letter.upper()
            if letter in "".join(temp_letters_2):
                temp_letters_2.remove(letter)
            else:
                return False
        return True

    
    def update(self, c:str):
        """
        Suma 1 a la frecuecia de la letra 'c' a la tabla de frecuencias

        Args:
            c(str) : letra que se agregara a la tabla de frecuencias
        """
        index = self.letters.index(c.lower())
        self.frequencies[index] += 1


###############################################################################
### EL TABLERO DE JUEGO
###############################################################################
class Board():
    score = 0 # Puntuacion total en el juego.
    
    def __init__(self) -> None:
        #Coordenadas/huecos dentro del tablero vacias por defectos
        self.board = np.full((15,15), ' ', dtype=str)
        self.totalWords = 0 #Numero total de palabras en el tablero.
        self.totalPawns = 0  #Numero total de fichas colocadas en el tablero.
        
    def showBoard(self):
        """
        Muestra el tablero
        """
        # Crear un array de 15x15 con valores cero
        grid = np.zeros((15, 15))
        # Crear la figura y los ejes
        fig, ax = plt.subplots()
        # Usar imshow para mostrar la cuadrícula
        cax = ax.imshow(grid, cmap = 'Greys')
        # Añadir líneas de cuadrícula
        ax.set_xticks(np.arange(-0.5, 15, 1), minor=True)
        ax.set_yticks(np.arange(-0.5, 15, 1), minor=True)
        ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
        # Configurar las etiquetas de los ticks en los ejes x e y
        ax.set_xticks(np.arange(0, 15, 1))
        ax.set_yticks(np.arange(0, 15, 1))
        ax.set_xticklabels(np.arange(0, 15, 1))
        ax.set_yticklabels(np.arange(0, 15, 1))
        # Quitar los ticks
        ax.tick_params(which='minor',bottom=False, left=False)
    
        # Añadir caracteres del tablero
        for i in range(15):
            for j in range(15):
                ax.text(j, i, self.board[i, j], va='center', ha='center', color='blue')
                
        # Mostrar el tablero
        plt.title('TABLERO DE JUEGO')
        plt.show()
    
    def placeWord(self, player_pawns:list, place_word:list, cord_x:int, cord_y:int, direction:str):
        """
        Coloca una palabra en el tablero

        Args:
            player_pawns (object): objeto de la clase Pawns, con las fichas del jugador.
            place_word (str list): La palabra que quiere colocar en el tablero
            cord_x (int): Coordenadas del eje x del tableto
            cord_y (int): Corrdenadas del eje y del tablero
            direction ('V' or 'H'): Direccion en al que se colocaran las fichas
        """
        
        for i, letter in enumerate(place_word):
            if direction == 'H':
                # Verifica si la letra ya esta en el tablero y la devuelve a la 
                # mano del jugador si es True.
                if self.board[cord_x][cord_y + i] == letter:
                    self.totalPawns -= 1
                    # Agrega la letra a la mano, para evitar problemas a la hora
                    # de eliminar las letras que forman la palabra de tu mano. 
                    if letter not in player_pawns.letters:
                        player_pawns.letters.append(letter)
                else:
                    self.board[cord_x][cord_y + i] = letter
                    Board.score += Pawns.points[letter]
            
            elif direction == 'V':
                # Verifica si la letra ya esta en el tablero y la devuelve a la 
                # mano del jugador si es True.
                if self.board[cord_x + i][cord_y] == letter:
                    self.totalPawns -= 1
                else:
                    self.board[cord_x + i][cord_y] = letter
                    Board.score += Pawns.points[letter] 
        
        self.totalWords += 1
        self.totalPawns += len(place_word)
        
    def isPossible(self, word, cord_x, cord_y, direction):
        """
        Verifica si cumple las reglas del juego la palabra que se va a
        colocar en el tablero
        """
        #La palabra no puede salirse de los limites del tablero:
        if direction == "H":
            if cord_x < 0 or cord_x + len(word)-1 > 15:
                message = "La palabra no puede salirse de los limites del tablero"
                return (False, message)
        elif direction == "V":
            if cord_y < 0 or cord_y + len(word)-1 > 15:
                message = "La palabra no puede salirse de los limites del tablero"
                return (False, message)
                               
        # La primera palabra debe tener al menos una ficha situada en la casilla central
        if self.totalWords == 0:
            if direction == "H" and cord_x == 7 and 7 in range(cord_y, cord_y + len(word)):
                message = "Ha sido posible colocar la palabra en el tablero"
                return (True, message)
            elif direction == "V" and cord_y == 7 and 7 in range(cord_x, cord_x + len(word)):
                message = "Ha sido posible colocar la palabra en el tablero"
                return (True, message)
            else: 
                message = "La primera palabra debe tener al menos una ficha en la casilla central (7, 7)"
                return(False, message)
        
        #Todas las palabras, a excepción de la primera, deben usar una ficha ya existente en el tablero.
        if self.totalWords > 0:
            flag = False
            if direction == "V":
                for i, letter in enumerate(word):
                    #comprueba que no se sale del tablero la palabra
                    if cord_x + i < 15:
                        if self.board[cord_x + i][cord_y] == letter:
                            flag = True
                        elif self.board[cord_x + i][cord_y] != ' ':
                            message = "No se puede superponer con otra palabra diferente."
                            return (False, message)                            
                    else:
                        message = "La palabra se excede del tablero"
                        return (False, message)
                    
            elif direction == "H":                      
                for i, letter in enumerate(word):
                    if cord_y + i < 15: 
                        if self.board[cord_x][cord_y + i] == letter:
                            flag = True
                        elif self.board[cord_x][cord_y + i] != ' ':
                            message = "No se puede superponer con otra palabra diferente."
                            return (False, message)  
                    else:
                        message = "La palabra se excede del tablero"
                        return (False, message)
                                          
            if not flag:
                message = "Debes usar una ficha ya existente en el tablero"
                return (False, message)
            
        #Hay que colocar al menos una nueva ficha en el tablero
        new_letter_placed = False
        for i, letter in enumerate(word):
            if direction == "H":
                if self.board[cord_x][cord_y + i] != letter:
                    new_letter_placed = True
                    break
            elif direction == "V":
                if self.board[cord_x + i][cord_y] != letter:
                    new_letter_placed = True
                    break
        if not new_letter_placed:
            message = "Hay que colocar al menos una nueva ficha en el tablero"
            return (False, message)                               
        
        # No puede haber una ficha al principio o al final de la palabra que 
        # se vaya a colocar sobre el tablero si ésta no pertenece a la palabra
        if direction == "H":
            #verifica si hay una ficha en el lado izquiedo de la palabra                       
            if cord_y > 0 and self.board[cord_x][cord_y - 1] != ' ':
                message = "No puede haber una ficha adyacente al inicio de la palabra"
                return (False, message)
            #verifica si hay una ficha en el lado derecho de la palabra    
            if cord_y + len(word) < 15 and self.board[cord_x][cord_y + len(word)] != ' ':
                message = "No puede haber una ficha adyacente al final de la palabra"
                return (False, message)
        
        elif direction == "V":
            #verifica si hay una ficha en el lado izquiedo de la palabra              
            if cord_x > 0 and self.board[cord_x - 1][cord_y] != ' ':
                message = "No puede haber una ficha adyacente al inicio de la palabra"
                return (False, message)
            #verifica si hay una ficha en el lado derecho de la palabra
            if cord_x + len(word) < 15 and self.board[cord_x + len(word)][cord_y] != ' ':
                message = "No puede haber una ficha adyacente al final de la palabra"
                return (False, message)           
    
        message = "Ha sido posible colocar la palabra en el tablero"
        return (True, message)
       
    def getPawns(self, word, cord_x, cord_y, direction):
        """
        Devuelve un objeto de la clase word con las fichas que faltan en el 
        tablero.

        Args:
            word (str): palabra que se va a colocar en el tablero
            cord_x (int): coordenadas del eje vertical
            cord_y (int): coordenadas del eje horizontal
            direction (V or H): Vertical o Horizontal

        Returns:
            class obejct: objeto work con las fichas que necesitas para 
                        formar la palabra en el tablero.
        """
        missing_pawns = Word()

        for i, letter in enumerate(word):
            if direction == 'H':
                # Verifica la letra no esta en el tablero
                if self.board[cord_x][cord_y + i] != letter:
                    #agrega la letra al diccionario de la clase word
                    missing_pawns.word.append(letter.lower())
            
            elif direction == 'V':
                # Verifica la letra no esta en el tablero
                if self.board[cord_x + i][cord_y] != letter:
                    #agrega la letra al diccionario de la clase word
                    missing_pawns.word.append(letter.lower())

        return missing_pawns
    
    def showWordPlacement(self, player_pawns, word):
        """
        Muestra por pantalla todas las posibles colocaciones de las fichas 
        en el tablero.
        """
        print("\nDirecciones permitidas para colocar en el tablero: ")
        posible_directions = 0
        for direction in (0, 1):
            for cord_x in range(0, 15):
                for cord_y in range(0,15):
                    if direction == 0:
                        checking = self.isPossible(word, cord_x, cord_y, "V")
                        if checking[0]:
                            posible_directions += 1
                            print(f"·Vertical:{cord_x}, Horizontal:{cord_y}, Direction:'V'")
                            
                    else:
                        checking = self.isPossible(word, cord_x, cord_y, "H")
                        if checking[0]:
                            posible_directions += 1
                            print(f"·Vertical:{cord_x}, Horizontal:{cord_y}, Direction:'H'")
        if posible_directions == 0:
            print("La palabra no se puede colocar en el tablero")
            print("Debe coincidir al menos una ficha con alguna palabra del tablero")
            return False
        return True
    
    def welcome(self):
        """
        Imprime un mensaje de bienvenida
        """
        welcome_file = r"D:\Programacion\Git_And_GitHub\Proyecto-python-fin-curso\datas\welcome_message.txt"
        
        with open (welcome_file, 'r') as f:
            file_content = f.read()
            
        print(file_content)
    
    def instructions(self):
        """
        Imprime las instrucciones del juego
        """
        welcome_file = r"D:\Programacion\Git_And_GitHub\Proyecto-python-fin-curso\datas\instructions_message.txt"
        
        with open (welcome_file, 'r') as f:
            file_content = f.read()
            
        print(file_content)  
            
        