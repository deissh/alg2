from tree import Tree, Node

from render import RenderTree

tree = Tree[int]()

tree.node = Node(
    value=1,
    children=[
        Node(
            value=3,
            children=[
                Node(
                    value=1,
                    children=[Node(
                        value=1
                    )]
                ),
                Node(
                    value=1
                ),
                Node(
                    value=4
                )
            ],
        ),
        Node(value=2)
    ]
)

print("stats")
print(f"count={tree.count}")
print(f"depth={tree.depth}")

print("\nrender tree")
for pre, _, node in RenderTree(tree):
    print(f"{pre}{node}")
