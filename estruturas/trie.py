"""
Aluno: Lucas Prado da Costa Burgos
lpcb@cin.ufpe.br
Projeto 2 - Algoritmos e Estruturas de dados(IF969)
28-10-2018
"""
import numpy as np
from memory_profiler import profile


class Node():
    def __init__(self, letra, valor=None):
        self.letra = letra
        self.valor = valor
        self.filhos = np.ndarray(shape=53, dtype=object)

class Trie():
    def __init__(self):
        self.root = Node(None)

    @staticmethod
    def procurar(letra):
        if letra <= 'z' and letra >= 'a':
            pos = ord(letra) - ord('a')
        elif letra >= 'A' and letra <= 'Z':
            pos = ord(letra) - ord('A') + 26
        else:
            pos = 52      
        return pos
    @profile
    def inserir(self, ngrama):
        frase = str(ngrama)
        local = self.root
        for letra in frase:
            pos = self.procurar(letra)
            if local.filhos[pos] is None:
                local.filhos[pos] = Node(letra)
            no = local.filhos[pos]
            local = local.filhos[pos]
        if no.valor is None:
            no.valor = []
        no.valor.append(ngrama.documento)


    def buscar(self, ngrama):
        frase = str(ngrama)
        local = self.root
        for letra in frase:
            pos = self.procurar(letra)
            if local.filhos[pos] is None:
                return False
            lastNode = local.filhos[pos]
            local = local.filhos[pos]
        if lastNode.valor is None:
            pass
        else:
            return lastNode.valor



    
        

