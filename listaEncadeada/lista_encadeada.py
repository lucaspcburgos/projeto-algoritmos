class Node():

    """
    Auxiliar na composição da classe lista encadeada
    cada objeto recebe 2 valores (currentElement e nextElement) sendo assim possível
    armazenar os dados de uma lista encadeada. Tais valores são nulos por padrão caso nenhum parâmetro
    seja passado.
    """

    def __init__(self, currentElement=None, nextElement=None):
        self.currentElement = currentElement
        self.nextElement = nextElement


class ListaEncadeada():

    """
    classe lista encadeada
    estrutura para armazenamento de dados, onde cada elemento (objeto da classe Node)
    tem seu atributo 'nextElement' apontando para um outro elemento (que também é uma instância da classe Node)
    até que um elemento aponta para None, sendo este tomado como o último elemento da lista encadeada.
    """

    def __init__(self):
        self.firstElement = Node()
        self.lastElement = Node()

    def __str__(self):
        if self.isEmpty():
            return '[]'
        string = '['
        aux = self.firstElement.nextElement
        while aux.nextElement:
            string += str(aux.currentElement) + ', '
            aux = aux.nextElement
        string += str(self.lastElement.currentElement.currentElement) + ']'
        return string

    def isEmpty(self):
        if not self.firstElement.nextElement and not self.lastElement.currentElement:
            return True

    def insertLast(self, element):

        """
        inserir elemento no final da lista
        caso a lista esteja vazia (primeiro elemento == ultimo elemento == None)
        deve se inserir o numero na primeira posição que é o firstElement.nextElement.
        Caso contrário, deve-se procurar o ultimo elemento e adicionar o novo elemento como sendo o ultimo.nextElement
        e depois atualizando o self.lastElement.currentElement == novo elemento
        """

        if self.isEmpty():
            self.firstElement.nextElement = Node(currentElement=element, nextElement=None)
            self.lastElement.currentElement = self.firstElement.nextElement

        else:
            self.lastElement.currentElement.nextElement = Node(currentElement=element, nextElement=None)
            self.lastElement.currentElement = self.lastElement.currentElement.nextElement

    def search(self,element):
        if self.isEmpty():
            return False
        else:
            listElement = self.firstElement.nextElement
            while listElement.nextElement:
                if listElement.currentElement == element:
                    print('aqui')
                    return True

                else:
                    listElement = listElement.nextElement
                    if listElement.currentElement is self.lastElement and self.lastElement.currentElement.currentElement != element:
                        return False
                    else:
                        return True

    def insertFirst(self, element):
        aux = self.firstElement.nextElement
        self.firstElement.nextElement = Node(currentElement=element, nextElement=aux)

    def delete(self):
        pass

    def size(self):
        s = 0
        i = self.firstElement.nextElement
        while i:
            s += 1
            i = i.nextElement
        return s


#==============================================TESTANDO LISTA ENCADEADA ================================================
"""
lista = ListaEncadeada()

print(lista)

dic = {
    'chave': 125
}

print(type(dic))

lista.insertLast(dic)
lista.insertLast(34)
lista.insertLast(4)
lista.insertFirst(12)
lista.insertLast(58)
lista.insertLast(61)
lista.insertLast(17)
lista.insertFirst(110)

if lista.search(4):
    print(lista)
"""