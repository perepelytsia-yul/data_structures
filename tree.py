class BinaryTreeNode:
    def __init__(self, data):
        self.__data = data
        self.leftChild = None
        self.rightChild = None

    def add_left_child(self, child):
        self.leftChild = child

    def get_left_child(self):
        return self.leftChild

    def remove_left_child(self):
        self.leftChild = None

    def add_right_child(self, child):
        self.rightChild = child

    def get_right_child(self):
        return self.rightChild

    def print_data(self):
        print(self.__data)

"""
root = BinaryTreeNode(50)
root.add_left_child(BinaryTreeNode(22))
root.get_left_child().print_data()
root.add_right_child(BinaryTreeNode(70))
root.get_right_child().print_data()
root.remove_left_child()
"""


class SortedBinaryTree:
    def __init__(self, data:int):
        self.__data = data
        self.leftChild = None
        self.rightChild = None

    def get_data(self):
        return self.__data

    def add_child(self, child):
        if child.get_data() <= self.__data:
            if self.get_left_child():
                self.get_left_child().add_child(child)
            else:
                self.leftChild = child
        else:
            if self.get_right_child():
                self.get_right_child().add_child(child)
            else:
                self.rightChild = child

    def get_left_child(self):
        return self.leftChild

    def get_right_child(self):
        return self.rightChild

    def print_data(self):
        print(self.__data)

    def check_value(self, value):
        if self.__data == value:
            return True
        elif self.__data > value:
            if self.get_left_child():
                return self.get_left_child().check_value(value)
            else:
                return False
        else:
            if self.get_right_child():
                return self.get_right_child().check_value(value)
            else:
                return False


root = SortedBinaryTree(77)
root.print_data()
root.add_child(SortedBinaryTree(55))
root.add_child(SortedBinaryTree(23))
root.add_child(SortedBinaryTree(7))
root.get_left_child().print_data()
root.get_left_child().get_left_child().print_data()
root.get_left_child().get_left_child().get_left_child().print_data()

print(root.check_value(23))

#root.get_right_child().print_data()