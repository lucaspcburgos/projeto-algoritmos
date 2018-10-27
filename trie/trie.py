import numpy as np

class Node():
    def __init__(self, letra, valor=None):
        self.letra = letra
        self.valor = valor
        self.filhos = np.ndarray(shape=53)

class Trie():
    def __init__(self):
        self.root = Node(None)
        self.primeiros = self.root.filhos
    @staticmethod
    def procurar(letra):
        if letra <= 'z' and letra >= 'a':
            pos = ord(letra) - ord('a')
        elif letra >= 'A' and letra >= 'Z':
            pos = ord(letra) - ord('A') + 26
        else:
            pos = 52      
        return pos

    def inserirLetra(self, letra):

        pos = self.procurar(letra)
        if not self.primeiros[pos]:
            self.primeiros[pos] = Node(letra)


    
        

