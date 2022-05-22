class Arr:
    __data__ = []

    def __init__(self):
        pass

    def append(self, el):
        if self.__data__:
            if isinstance(el, type(self.__data__[0])):
                self.__data__.append(el)
        else:
            self.__data__.append(el)

    def __str__(self):
        test_str = ""
        for i in self.__data__:
            test_str += (str(i) + " ")
        return test_str


test = Arr()
test.append(4)
test.append(8)
print(test)
