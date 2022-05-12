import random
from typing import TypeVar

from node import Node
from tree import Tree
from main import print_tree


T = TypeVar("T")


class KLeftTree(Tree[T]):
    n: int

    def __init__(self, n: int):
        super(KLeftTree, self).__init__()
        self.n = n

    def add(self, value: T):
        if self.is_empty:
            self.node = Node(value=value, children=[None, None])

        self.__add(self.node, value)

    def __add(self, node: Node[T], value: T):
        if node.count < self.n:
            if node.children[0] is not None:
                self.__add(node.children[0], value)
            else:
                node.children[0] = Node(value=value, children=[None, None])
        else:
            if node.children[1] is not None:
                self.__add(node.children[1], value)
            else:
                node.children[1] = Node(value=value, children=[None, None])


if __name__ == "__main__":
    tree = KLeftTree[int](4)

    for _ in range(9):
        tree.add(random.randint(0, 10))

    print_tree(tree)
