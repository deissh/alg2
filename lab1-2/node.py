from __future__ import annotations

import uuid
from typing import TypeVar, Generic, List, Optional, Iterable, Tuple
from dataclasses import dataclass, field

T = TypeVar('T')


@dataclass
class Node(Generic[T]):
    value: T

    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    children: List[Optional[Node]] = field(default_factory=list)

    def __str__(self):
        return f"Node(id={self.id}, value={self.value})"

    @property
    def depth(self) -> int:
        max_depth = 0

        for _, level in self:
            max_depth = max(max_depth, level)

        return max_depth

    @property
    def count(self) -> int:
        return len(list(self))

    def find(self, _id: str) -> Optional[Node[T]]:
        for node, _ in self:
            if node.id == _id:
                return node

        return None

    def __iter__(self) -> Iterable[Tuple[Node, int]]:
        return self.__next(self)

    def __next(self, node: Node[T], level=0) -> Iterable[Tuple[Node, int]]:
        yield node, level

        level += 1
        for child in node.children:
            if child is None:
                continue

            for grandchild, level in self.__next(child, level):
                yield grandchild, level

