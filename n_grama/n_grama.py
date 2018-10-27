class Ngrama():
    def __init__(self, first, last, document):
        self.__first = first
        self.__last = last
        self.__document = document

    def __contains__(self, palavra):
        arr = self.__document.returnArray[self.__first:self.__last+1]
        for i in arr:
            if arr == palavra:
                return True
        return False
            

    def __eq__(self,ngramaDocument):
        if self.__document.returnArray[self.__first:self.__last+1] == ngrama.__document.returnArray[self.__first:self.__last+1]:
            return True
        else:
            return False

    def __repr__(self):
        return '{0}({1},{2},{3})'.format(self.__class__.__name__,self.__first, self.__last, repr(self.__document))
