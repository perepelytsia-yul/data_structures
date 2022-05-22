class Stack:
    __data__ = []

    def __init__(self):
        pass

    def push(self, item):
        self.__data__.append(item)

    def pop(self):
        if self.__data__:
            poped_item = self.__data__.pop(-1)
            return poped_item
        else:
            return None

    def __str__(self):
        test_str = ""
        for i in self.__data__:
            test_str += (str(i) + " ")
        return test_str


stack = Stack()
stack.push(999)
print(stack)
stack.push(50)
print(stack)
stack.push(1)
print(stack)
print("-----------")
print(stack.pop())
print(stack)

