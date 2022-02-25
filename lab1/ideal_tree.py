from typing import TypeVar, Optional
from operator import sub

from lab1.render import Render
from node import Node

T = TypeVar("T")


def ibal(n: int = 0) -> Optional[Node[T]]:
    if n <= 0:
        return None

    new_node = Node(n)

    l_node = ibal(n // 2)
    if l_node is not None:
        new_node.children.append(l_node)
    r_node = ibal(n - n // 2 - 1)
    if r_node is not None:
        new_node.children.append(r_node)

    return new_node


def is_ideal(node: Node[T]) -> bool:
    if node is None:
        return False

    if len(node.children) < 2:
        return False

    diff = [
        node.children[0].depth,
        node.children[1].depth,
    ]

    return abs(sub(*diff)) <= 1


if __name__ == "__main__":
    node = ibal(2)

    print("ideal", is_ideal(node))

    for pre, _, s in Render(node):
        print(f"{pre}{s}")
