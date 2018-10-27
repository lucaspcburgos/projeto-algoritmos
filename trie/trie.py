import numpy as np

class Node():
    def __init__(self, letra, valor=None):
        self.letra = letra
        self.valor = valor
        self.filhos = np.ndarray(shape=50)

class Trie():
    def __init__(self):
        self.root = Node()

    def inserirLetra(self, letra):
        if letra <= 'z' and letra >= 'a':
            pos = ord(letra) - ord('a')
        elif letra >= 'A' and letra >= 'Z':



