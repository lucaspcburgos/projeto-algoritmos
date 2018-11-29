"""
Aluno: Lucas Prado da Costa Burgos
lpcb@cin.ufpe.br
Projeto 2 - Algoritmos e Estruturas de dados(IF969)
28-10-2018
"""

from memory_profiler import profile
import os
from estruturas.documento import Documento
from estruturas.trie import Trie


class Corpus():

    """
    Essa classe recebe o caminho para uma pasta onde cada arquivo txt armazenado na mesma
    é passado como parametro para a instancia da classe Documento() na variavel file dentro do método construtor,
    criando assim uma lista (self.docs) onde cada elemento é um objeto de Documento() com um array de todas as palavras de cada
    documento txt da pasta recebida
    """
    @profile
    def __init__(self, path, n):
        self.__n = n
        self.__docs = []
        self.__arvoreTrie = Trie()

        filelist = os.listdir(path)
        for i in filelist[0:1]:
            if i.endswith(".txt"):
                docPath = str(path) + str(i)
                file = Documento(docPath, self.__n)
                self.__docs.append(file)
        for doc in self.__docs:
            listaEncadeadaDeNgramas = doc.gerarNgramas()
            aux = listaEncadeadaDeNgramas.firstElement.nextElement
            while aux.nextElement:
                self.__arvoreTrie.inserir(aux.currentElement)
                aux = aux.nextElement
            self.__arvoreTrie.inserir(listaEncadeadaDeNgramas.lastElement.currentElement.currentElement)
            print('inseriu: ', doc.file)

    @property
    def n(self):
        return self.__n

    @property
    def docs(self):
        return self.__docs

    @property
    def arvoreTrie(self):
        return self.__arvoreTrie

    @profile
    def verificarPlagio(self, file, limiar):

        """
        Esse metodo recebe o caminho de um arquivo (file) que vai ser analisado para definir se é plágio ou não.
        Esse mesmo arquivo é passado como parametro para o metodo contençao() de cada elemento d em self.docs e como
        o metodo retorna uma medida de contençao, ele é comparada com o limiar passado como parametro, e todos aqueles
        documentos que possuirem uma medida maior ou igual ao limiar, são retornados em uma lista.

        """
        docSuspeito = Documento(file, self.__n)
        docSuspeito.gerarNgramas()
        dicResultado = docSuspeito.contencao(self.__arvoreTrie)
        listaResultados = list(dicResultado.values())
        listaFinal = []
        for doc in listaResultados:
            if doc[1] >= limiar:
                listaFinal.append(doc)
        return listaFinal
