class Node:
    def __init__(self,currentElement=None,nextElement=None):
        self.currentElement = currentElement
        self.nextElement = nextElement

class ListaEncadeada:
    def __init__(self):
        self.firstElement = Node()
        self.lastElement = Node()        
    def empty(self):
        if self.firstElement.nextElement == None:
            return True
        else:
            return False
    def insertAtEnd(self, element):
        newElement = Node(element,None)
        if self.empty():
            self.firstElement.nextElement = newElement
            self.lastElement.currentElement = self.firstElement.nextElement 
        else:
            self.lastElement.nextElement = newElement  
"""
    def empty(self):
        if self.firstElement.nextElement == self.lastElement.nextElement:
            return True

    def insertAtEnd(self,element):
        if self.empty():                        
            self.firstElement.nextElement = Node(element,None)
            self.lastElement.currentElement = self.firstElement.nextElement
        else:
            self.lastElement.nextElement = Node(element)
            self.lastElement = self.lastElement.nextElement
    
    def contains(self, element):        
        aux = self.firstElement.nextElement             
        while aux != element:
            aux = aux.nextElement
            if aux.nextElement == None:
                return False
        return True

a = ListaEncadeada()
a.empty()
for i in range(10):
    a.insertAtEnd(i)
if a.contains(2):
    print('ok')
else:
    print('not')
"""   
