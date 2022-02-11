import collections
from typing import TypeVar, Generic, Tuple, Iterable

from tree import Tree, Node

Row = collections.namedtuple("Row", ("pre", "fill", "node"))

T = TypeVar("T")


class RenderStyle(object):
    vertical: str
    cont: str
    end: str

    @property
    def empty(self):
        return self.vertical + " " * (len(self.end) - 1)


class AsciiStyle(RenderStyle):
    vertical = "|"
    cont = "|-- "
    end = "+-- "


class RenderTree(Generic[T]):
    node: Node[T]
    style: RenderStyle

    def __init__(self, tree: Tree[T], style: RenderStyle = AsciiStyle()):
        self.node = tree.node
        self.style = style

    def __iter__(self) -> Iterable[Row]:
        return self.__next(self.node, tuple())

    def __next(self, node: Node[T], continues: Tuple, level=0) -> Iterable[Row]:
        yield RenderTree.__item_render(node, continues, self.style)

        level += 1
        for child in node.children:
            if child is None:
                continue

            for grandchild in self.__next(child, continues + (not RenderTree.__is_last, ), level=level):
                yield grandchild

    @staticmethod
    def __item_render(node: Node[T], continues: Tuple, style: RenderStyle) -> Row:
        if not continues:
            return Row(u'', u'', node)
        else:
            items = [style.empty for _ in continues]
            indent = ''.join(items[:-1])
            branch = style.cont if continues[-1] else style.end
            pre = indent + branch
            fill = ''.join(items)
            return Row(pre, fill, node)

    @staticmethod
    def __is_last(iterable) -> Tuple[Node, bool]:
        iter_ = iter(iterable)
        try:
            next_item = next(iter_)
        except StopIteration:
            pass
        else:
            item = next_item
            while True:
                try:
                    next_item = next(iter_)
                    yield item, False
                except StopIteration:
                    yield next_item, True
                    break
                item = next_item
