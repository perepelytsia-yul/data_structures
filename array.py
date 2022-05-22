class Arr:
    __data__ = []

    def __init__(self):
        pass

    def append(self, el):
        if self.__data__:
            if isinstance(el, type(self.__data__[0])):
                self.__data__.append(el)
            else:
                print("Data in Arr can be only of one Data type!!!")
        else:
            self.__data__.append(el)

    def __str__(self):
        bobo = ""
        for i in self.__data__:
            bobo += str(i)
        return bobo


test = Arr()
test.append(4)
test.append(8)
print(test)
