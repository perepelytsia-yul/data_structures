class Queue:
    __data__ = []

    def __init__(self):
        pass

    def push(self, item):
        self.__data__.append(item)

    def pop(self):
        if self.__data__:
            popped_item = self.__data__.pop(0)
            return popped_item
        else:
            return None

    def __str__(self):
        test_str = ""
        for i in self.__data__:
            test_str += (str(i) + " ")
        return test_str


queue = Queue()
queue.push(999)
print(queue)
queue.push(50)
print(queue)
queue.push(1)
print(queue)
print("-----------")
print(queue.pop())
print(queue)
