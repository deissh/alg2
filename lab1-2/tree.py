from typing import Optional, TypeVar, Generic, Iterable, Tuple

from node import Node

T = TypeVar("T")


class EmptyTreeError(Exception):
    pass


class Tree(Generic[T]):
    node: Optional[Node[T]]

    def __init__(self):
        self.node = None

    def __getitem__(self, _id: str) -> Optional[Node[T]]:
        for node, _ in self:
            if node.id == _id:
                return node

        return None

    @property
    def is_empty(self) -> bool:
        return self.node is None

    @property
    def count(self) -> int:
        if self.is_empty:
            raise EmptyTreeError

        return len(list(self))

    @property
    def depth(self) -> int:
        if self.is_empty:
            raise EmptyTreeError

        max_depth = 0

        for _, level in self:
            max_depth = max(max_depth, level)

        return max_depth

    def __iter__(self) -> Iterable[Tuple[Node, int]]:
        if self.is_empty:
            raise EmptyTreeError

        return self.__next(self.node)

    def __next(self, node: Node[T], level=0) -> Iterable[Tuple[Node, int]]:
        yield node, level

        level += 1
        for child in node.children:
            if child is None:
                continue

            for grandchild, level in self.__next(child, level):
                yield grandchild, level
