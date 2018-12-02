class Matriz():
    """
    Essa classe constroi uma matriz
    """
    def __init__(self, lines, columns):
        """
        Cria uma matriz
        :param lines: numero de linhas da matriz
        :param columns: numero de colunas da matriz
        """
        m = []
        for i in range(lines + 1):
            m.append([None]*(columns+1))
        self.table = m

    def insertPosition(self, line, column, element):
        """
        Esse metodo insere um elemento em uma determinada posiçao da matriz
        :param line: linha que o elemento deve ser inserido
        :param column: coluna que o elemento deve ser inserido
        :param element: elemento a ser inserido
        """
        self.table[line][column] = element

    def find(self, line, column):
        """
        acessa uma posiçao informada e retorna elemento que se encontra nela
        :param line: linha da posiçao que procuramos
        :param column: coluna da posiçao que procuramos
        :return: elemento nessa posiçao
        """
        return self.table[line][column]


    def __str__(self):
        s = '['
        for linha in self.table:
            s += str(linha) + ',\n'
        s += ']'
        return s


class Maximaze():
    def __init__(self, maxWeight, maxItems, itemsWeights, itemsValues):
        """
        classe que calcula a melhor combinaçao de elementos com determinados pesos e valores de forma que o valor resulatante
        seja maximo e a soma dos pesos nao exceda o limite passado
        :param maxWeight: inteiro, limite maximo de peso
        :param maxItems: inteiro, quantidade de itens a serem analizados
        :param itemsWeights: lista com os pesos dos elementos
        :param itemsValues: lista com os valores dos elementos
        """
        self.matrix = Matriz(maxItems, maxWeight)
        self.__items = []

        for item in range(maxItems + 1):
            for w in range(maxWeight + 1):

                if w == 0 or item == 0:
                    self.matrix.insertPosition(item, w, 0)

                elif itemsWeights[item-1] > w:
                    value = self.matrix.find(item-1, w)
                    self.matrix.insertPosition(item, w, value)

                else:
                    value = max(self.matrix.find(item-1, w), self.matrix.find(item-1, w - itemsWeights[item-1] ) + itemsValues[item-1])
                    self.matrix.insertPosition(item, w, value)

        #print(self.matrix)

        self.__maxValue = self.matrix.find(maxItems, maxWeight)

        for i in range(maxItems, 0, -1):
            if self.matrix.find(i, maxWeight) != self.matrix.find(i-1, maxWeight):
                self.__items.append((itemsValues[i-1], itemsWeights[i-1]))
                maxWeight -= itemsWeights[i - 1]

    @property
    def items(self):
        return self.__items

    @property
    def value(self):
        return self.__maxValue
