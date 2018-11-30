class Matriz():
    def __init__(self, lines, columns):
        m = []
        for i in range(lines + 1):
            m.append([None]*(columns+1))
        self.table = m

    def insertPosition(self, line, column, element):
        self.table[line][column] = element

    def find(self, line, column):
        return self.table[line][column]


    def __str__(self):
        s = '['
        for linha in self.table:
            s += str(linha) + ',\n'
        s += ']'
        return s


class Maximaze():
    def __init__(self, maxWeight, maxItems, itemsWeights, itemsValues):
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

        print(self.matrix)

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



if __name__ == '__main__':
    a = Maximaze(maxWeight=5, maxItems=5, itemsWeights=[2, 5, 3, 1, 6], itemsValues=[10, 35, 23, 41, 9])