from __future__ import annotations

import math
import random
from typing import Any


class Queue:
    def __init__(self) -> None:
        self.data: list[Any] = []
        self.head: int = 0
        self.tail: int = 0

    def is_empty(self) -> bool:
        return self.head == self.tail

    def push(self, data: Any) -> None:
        self.data.append(data)
        self.tail = self.tail + 1

    def pop(self) -> Any:
        ret = self.data[self.head]
        self.head = self.head + 1
        return ret

    def count(self) -> int:
        return self.tail - self.head

    def print(self) -> None:
        print(self.data)
        print("**************")
        print(self.data[self.head : self.tail])


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.left: Node | None = None
        self.right: Node | None = None
        self.height: int = 1

    def get_data(self) -> Any:
        return self.data

    def get_left(self) -> Node | None:
        return self.left

    def get_right(self) -> Node | None:
        return self.right

    def get_height(self) -> int:
        return self.height

    def set_data(self, data: Any) -> None:
        self.data = data
        return

    def set_left(self, node: Node | None) -> None:
        self.left = node
        return

    def set_right(self, node: Node | None) -> None:
        self.right = node
        return

    def set_height(self, height: int) -> None:
        self.height = height
        return


def get_height(node: Node | None) -> int:
    if node is None:
        return 0
    return node.get_height()


def my_max(a: int, b: int) -> int:
    if a > b:
        return a
    return b


def right_rotation(node: Node) -> Node:
    print("left rotation node:", node.get_data())
    ret = node.get_left()
    assert ret is not None
    node.set_left(ret.get_right())
    ret.set_right(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    ret.set_height(h2)
    return ret


def left_rotation(node: Node) -> Node:
    print("right rotation node:", node.get_data())
    ret = node.get_right()
    assert ret is not None
    node.set_right(ret.get_left())
    ret.set_left(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    h2 = my_max(get_height(ret.get_right()), get_height(ret.get_left())) + 1
    ret.set_height(h2)
    return ret


def lr_rotation(node: Node) -> Node:
    left_child = node.get_left()
    assert left_child is not None
    node.set_left(left_rotation(left_child))
    return right_rotation(node)


def rl_rotation(node: Node) -> Node:
    right_child = node.get_right()
    assert right_child is not None
    node.set_right(right_rotation(right_child))
    return left_rotation(node)


def insert_node(node: Node | None, data: Any) -> Node | None:
    if node is None:
        return Node(data)
    if data < node.get_data():
        node.set_left(insert_node(node.get_left(), data))
        if (
            get_height(node.get_left()) - get_height(node.get_right()) == 2
        ):  # an unbalance detected
            left_child = node.get_left()
            assert left_child is not None
            if (
                data < left_child.get_data()
            ):  # new node is the left child of the left child
                node = right_rotation(node)
            else:
                node = lr_rotation(node)
    else:
        node.set_right(insert_node(node.get_right(), data))
        if get_height(node.get_right()) - get_height(node.get_left()) == 2:
            right_child = node.get_right()
            assert right_child is not None
            if data < right_child.get_data():
                node = rl_rotation(node)
            else:
                node = left_rotation(node)
    h1 = my_max(get_height(node.get_right()), get_height(node.get_left())) + 1
    node.set_height(h1)
    return node


def get_rightMost(root: Node) -> Any:
    while True:
        right_child = root.get_right()
        if right_child is None:
            break
        root = right_child
    return root.get_data()


def get_leftMost(root: Node) -> Any:
    while True:
        left_child = root.get_left()
        if left_child is None:
            break
        root = left_child
    return root.get_data()


def del_node(root: Node, data: Any) -> Node | None:
    left_child = root.get_left()
    right_child = root.get_right()
    if root.get_data() == data:
        if left_child is not None and right_child is not None:
            temp_data = get_leftMost(right_child)
            root.set_data(temp_data)
            root.set_right(del_node(right_child, temp_data))
        elif left_child is not None:
            root = left_child
        elif right_child is not None:
            root = right_child
        else:
            return None
    elif root.get_data() > data:
        if left_child is None:
            print("No such data")
            return root
        else:
            root.set_left(del_node(left_child, data))
    else:  # root.get_data() < data
        if right_child is None:
            return root
        else:
            root.set_right(del_node(right_child, data))

    if get_height(right_child) - get_height(left_child) == 2:
        assert right_child is not None
        if get_height(right_child.get_right()) > get_height(right_child.get_left()):
            root = left_rotation(root)
        else:
            root = rl_rotation(root)
    elif get_height(right_child) - get_height(left_child) == -2:
        assert left_child is not None
        if get_height(left_child.get_left()) > get_height(left_child.get_right()):
            root = right_rotation(root)
        else:
            root = lr_rotation(root)
    height = my_max(get_height(root.get_right()), get_height(root.get_left())) + 1
    root.set_height(height)
    return root


class AVLtree:
    def __init__(self) -> None:
        self.root: Node | None = None

    def get_height(self) -> int:
        return get_height(self.root)

    def insert(self, data: Any) -> None:
        print("insert:" + str(data))
        self.root = insert_node(self.root, data)

    def del_node(self, data: Any) -> None:
        print("delete:" + str(data))
        if self.root is None:
            print("Tree is empty!")
            return
        self.root = del_node(self.root, data)

    def __str__(
        self,
    ) -> str:  # a level traversale, gives a more intuitive look on the tree
        output = ""
        q = Queue()
        q.push(self.root)
        layer = self.get_height()
        if layer == 0:
            return output
        cnt = 0
        while not q.is_empty():
            node = q.pop()
            space = " " * int(math.pow(2, layer - 1))
            output += space
            if node is None:
                output += "*"
                q.push(None)
                q.push(None)
            else:
                output += str(node.get_data())
                q.push(node.get_left())
                q.push(node.get_right())
            output += space
            cnt = cnt + 1
            for i in range(100):
                if cnt == math.pow(2, i) - 1:
                    layer = layer - 1
                    if layer == 0:
                        output += "\n*************************************"
                        return output
                    output += "\n"
                    break
        output += "\n*************************************"
        return output


def _test() -> None:
    import doctest

    doctest.testmod()


if __name__ == "__main__":
    _test()
    t = AVLtree()
    lst = list(range(10))
    random.shuffle(lst)
    for i in lst:
        t.insert(i)
        print(str(t))
    random.shuffle(lst)
    for i in lst:
        t.del_node(i)
        print(str(t))
