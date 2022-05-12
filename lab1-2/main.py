import json
import random

from bin_tree import BTree
from render import Render

from utils import EnhancedJSONEncoder

random.seed(1)


def print_tree(tree):
    print("stats")
    print(f"count={tree.count}")
    print(f"depth={tree.depth}")

    print("\nrender tree")
    for pre, _, node in Render(tree.node):
        print(f"{pre}{node}")


if __name__ == '__main__':
    print("\n\nBinTree")

    btree = BTree[int]()

    for _ in range(9):
        btree.add(random.randint(0, 10))

    # btree.rm(36)
    print_tree(btree)

    with open("tree.dump.json", "w+") as f:
        f.write(json.dumps(btree.node, cls=EnhancedJSONEncoder, indent=2))
