from typing import TypeVar, Optional

from tree import Tree, Node, EmptyTreeError

T = TypeVar("T")


class BTree(Tree[T]):
    def add(self, value: T):
        if self.is_empty:
            raise EmptyTreeError

        self.__add(self.node, value)

    def __add(self, node: Node[T], value: T):
        if node.value < value:
            if node.children[0] is not None:
                self.__add(node.children[0], value)
            else:
                node.children[0] = Node(value=value)
        else:
            if node.children[1] is not None:
                self.__add(node.children[1], value)
            else:
                node.children[1] = Node(value=value)

    def rm(self, value: T):
        pass

    def search(self, value: T) -> Optional[Node[T]]:
        if self.is_empty:
            raise EmptyTreeError

        return self.__search(self.node, value)

    def __search(self, node: Optional[Node[T]], value: T) -> Optional[Node[T]]:
        if node is None:
            return None

        if node.value == value:
            return node

        if node.value < value:
            return self.__search(node.children[0], value)
        if node.value > value:
            return self.__search(node.children[1], value)
