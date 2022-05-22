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
            if root.get_left_child():
                self.add_left_child(child)
            else:
                self.add_left_child(child)
        else:
            self.add_right_child(child)

    def add_left_child(self, child):
        self.leftChild = child

    def add_right_child(self, child):
        self.rightChild = child

    def get_left_child(self):
        return self.leftChild

    def get_right_child(self):
        return self.rightChild

    def print_data(self):
        print(self.__data)


root = SortedBinaryTree(77)
root.print_data()
root.add_child(SortedBinaryTree(55))
root.get_left_child().print_data()
#root.get_right_child().print_data()