class Node:
    def __init__(self,currentElement=None,nextElement=None):
        self.currentElement = current
        self.next = nextElement

class ListaEncadeada:
    def __init__(self):
        self.firstElement = Node()
        self.lastElement = Node()

    def empty(self):
        if self.firstElement == self.lastElement:
            return True

    def insertAtEnd(self,element):
        self.lastElement.nextElement = Node(element)
    
    def inList(self, element):        
        aux = self.firstElement
        while aux.currentElement != element:
            aux = aux.nextElement
            if aux.nextElement == None:
                return False
        return True
