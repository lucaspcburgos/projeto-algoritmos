import numpy as np
from listaEncadeada.lista_encadeada import ListaEncadeada
from n_grama.n_grama import Ngrama
#from memory_profiler import profile


class Documento():
    """
    essa classe recebe o caminho de um arquivo(file) e a quantidade de gramas a serem gerados(n)
    e armazena em um array (self.wordsArray) a cada palavra do documento aberto
    """
    def __init__(self,file,n):
        self.file = file
        self.wordsArray = np.array(open(file, 'r').read().split())
        self.n = n
        self.lista = ListaEncadeada()

    def returnArray():
        return self.wordsArray

    #@profile
    def gerarNgramas(self):
        """
        Esse metodo gera os n-gramas de tamanho self.n e armazena-os numa lista encadeada implementada no arquivo
        lista_encadeada.py , que é a self.lista
        """

        n = self.n
        for i in range(len(self.wordsArray)):
            data = self.wordsArray[i:n]
            nGrama = Ngrama(data)
            self.lista.insertLast(nGrama)
            n += 1
            if data[-1] == self.wordsArray[-1]:
                return self.lista
        return self.lista

    #@profile
    def contencao(self, doc):
        """
        esse metodo recebe o caminho de um arquivo a ser analisado e adiciona todas as suas palavras em um array,
        posteriormente gera seus n-gramas e os compara um a um com os da self.lista
        """
        lista2 = ListaEncadeada()
        secondFile = np.array(open(doc, 'r').read().split())
        n = self.n
        for i in range(len(secondFile)):
            data = secondFile[i:n]
            nGrama = Ngrama(data)
            lista2.insertLast(nGrama)
            n += 1
            if data[-1] == secondFile[-1]:
                break
        total = lista2.size()
        cont = 0
        j = self.lista.firstElement.nextElement
        k = lista2.firstElement.nextElement
        while j:
            while k:
                if np.array_equal(j.currentElement.data, k.currentElement.data):
                    cont += 1
                k = k.nextElement
            k = lista2.firstElement.nextElement
            j = j.nextElement

        medida = cont/total
        return medida

    def __repr__(self):
        return '{0}({1},{2})'.format(self.__class__.__name__, repr(self.file), self.n)

if __name__ == "__main__":
    d = Documento("teste.txt", 3)
    n = Ngrama(0, 3, d)
    repr(d)
    repr(n)