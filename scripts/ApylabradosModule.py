import numpy as np
import csv
import random

class Pawns():
    def __init__(self, letters: str = None):
        """Crear la bolsa de fichas (pawns) del juegos

        Args:
            letters (str, optional): _bolsa con las fichas/letras_. Defaults to np.empty((0)).
        """
        self.letters = letters
        if letters is None:
            self.letters = []
        else:
            self.letters = letters.copy()
    
    def addPawn(self, c: str):
        """Añade una pieza(pawn) al conjunto de letras

        Args:
            c (str): letra a añadir
        """
        self.letters.append(c)
    
    def addPawns(self, c: str, n: int):
        """Añadir Varias fichas a la vez de la misma letra

        Args:
            c (str): Letra de la ficha
            n (int): Numero de fichas a añadir
        """
        for time in range(n):
            self.addPawn(c)
    
    def createBag(self):
        """Crea la bolsa de fichas inicial a partir de archivo
            bag_of_pawns.csv
        """
        bags_of_pawns = r"D:\Programacion\Git_And_GitHub\Proyecto-python-fin-curso\datas\bag_of_pawns.csv"
        with open(bags_of_pawns, "r") as file:
            reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                if isinstance(row[1], float):
                    self.addPawns(row[0], int(row[1]))
    
    def showPawns(self):
        """Muestra el numero de fichas que hay en la bolsa
        """
        total_pawns = len(self.letters)
        if total_pawns > 0:
            print(f"Numero total de fichas: {total_pawns}")
            return self.getFrecuency()
        else:
            print("La bolsa de fichas esta vacia")
            return {}
    
    def takeRandomPawn(self):
        """Agarra una ficha aleatoria de la bolsa y la elimina de la bolsa.
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
        if w in self.word:
            return True
        return False
    
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
        input_word = input().strip().upper()
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
        frequency = FrecuencyTable()
        for letter in self.word[0]:
            frequency.update(letter)
        return frequency.showFrequency()                 
    
class Dictionary():
    filepath = r"D:\Programacion\Git_And_GitHub\Proyecto-python-fin-curso\datas\dictionary.txt"
    
    @staticmethod
    def validateWord(word:str):
        """
        Comprueba si una palabra esta en el diccionario
        """
        file = open(Dictionary.filepath, 'r')
        while True:
            readed_line = Word.readWordFromFile(file)
            if word.areEqual(readed_line):
                file.close()
                return True
            if readed_line == "":
                file.close()
                print("La palabra no se encuentra en el diccionario")
                return False


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