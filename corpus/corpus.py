#from memory_profiler import profile
import os
from documento.documento import Documento

class Corpus():

    """
    Essa classe recebe o caminho para uma pasta onde cada arquivo txt armazenado na mesma
    é passado como parametro para a instancia da classe Documento() na variavel file dentro do método construtor,
    criando assim uma lista (self.docs) onde cada elemento é um objeto de Documento() com um array de todas as palavras de cada
    documento txt da pasta recebida
    """
    #@profile
    def __init__(self, path, n):
        self.n = n
        self.docs = []
        filelist = os.listdir(path)
        for i in filelist:
            if i.endswith(".txt"):
                docPath = str(path) + str(i)
                file = Documento(docPath, self.n)
                self.docs.append(file)

    #@profile
    def verificarPlagio(self, file, limiar):

        """
        Esse metodo recebe o caminho de um arquivo (file) que vai ser analisado para definir se é plágio ou não.
        Esse mesmo arquivo é passado como parametro para o metodo contençao() de cada elemento d em self.docs e como
        o metodo retorna uma medida de contençao, ele é comparada com o limiar passado como parametro, e todos aqueles
        documentos que possuirem uma medida maior ou igual ao limiar, são retornados em uma lista.

        """
        lista = []
        for d in self.docs:
            d.gerarNgramas()
            l = d.contencao(file)
            print(l, '\n')
            if l >= limiar:
                lista.append(d)
        return lista
