"""
Aluno: Lucas Prado da Costa Burgos
lpcb@cin.ufpe.br
Projeto 2 - Algoritmos e Estruturas de dados(IF969)
28-10-2018
"""

import numpy as np
from estruturas.lista_encadeada import ListaEncadeada
from estruturas.n_grama import Ngrama
from memory_profiler import profile


class Documento():
    """
    essa classe recebe o caminho de um arquivo(file) e a quantidade de gramas a serem gerados(n)
    e armazena em um array (self.wordsArray) cada palavra do documento aberto
    """
    @profile
    def __init__(self,file,n):
        self.file = file
        self.wordsArray = np.array(open(file, 'r').read().split())
        self.n = n
        self.lista = ListaEncadeada()

    def returnArray(self):
        return self.wordsArray

    @profile
    def gerarNgramas(self):
        """
        Esse metodo gera os n-gramas de tamanho self.n e armazena-os numa lista encadeada implementada no arquivo
        lista_encadeada.py , que é a self.lista
        """

        n = self.n
        limit = len(self.wordsArray)
        for i in range(limit):
            newNgrama = Ngrama(i, n-1, self)
            self.lista.insertLast(newNgrama)
            n += 1
            if n > limit:
                break
        return self.lista


    @profile
    def contencao(self, trie):
        """
        :trie: arvore trie de n-gramas.

        esse metodo recebe uma arvore Trie e procura os proprios N-gramas desse objeto da classe Documentona arvore,
        retornando um dicionario com as chave sendo os nomes dos documentos e os valores sendo uma tupla com o numero
        de ocorrencias e a contençao, nessa ordem.
        """
        ngramasIguais = {}
        aux = self.lista.firstElement.nextElement
        while aux.nextElement:
            docList = trie.buscar(aux.currentElement)
            if docList:
                for doc in docList:
                    if doc.file not in ngramasIguais:
                        ngramasIguais[doc.file] = [1, 0, doc.file]
                        contencao = ngramasIguais[doc.file][0] / doc.lista.size()
                        ngramasIguais[doc.file] = [1, contencao, doc.file]
                    else:
                        n = ngramasIguais[doc.file][0] + 1
                        contencao = ngramasIguais[doc.file][0] / doc.lista.size()
                        if contencao == 1:
                            break
                        ngramasIguais[doc.file] = [n, contencao, doc.file]
            aux = aux.nextElement
        return ngramasIguais

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, repr(self.file), self.n)
