import numpy as np
import csv

class Pawns():
    def __init__(self, letters: str = np.empty((0))):
        """Crear la bolsa de fichas (pawns) del juegos

        Args:
            letters (str, optional): _bolsa con las fichas/letras_. Defaults to np.empty((0)).
        """
        self.letters = letters
    
    def addPawn(self, c: str):
        """Añade una pieza(pawn) al conjunto de letras

        Args:
            c (str): letra a añadir
        """
        self.letters = np.append(self.letters, c)
    
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
            pawns_count = {}
            for pawn in self.letters:
                if pawn in pawns_count:
                    pawns_count[pawn] += 1
                else:
                    pawns_count[pawn] = 1
            print(pawns_count)
        else:
            print("La bolsa de fichas esta vacia") 
