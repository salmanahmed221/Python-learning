from typing import TypeVar, Generic

T = TypeVar("T")


class Node(Generic[T]):
    x: T

    def __init__(self, x: T) -> None:
        self.x = x


x1 = Node("")  # Inferred type is Node[str]
y1 = Node(0)  # Inferred type is Node[int]
z1 = Node(True)  # Inferred type is Node[Any]

a122 = Node[int](0)
b12 = Node[str]("a")
b121 = Node[bool](False)
a1211 = Node[tuple[int, int, int]]((1, 2, 3))
d1211 = Node[list[int]]([1, 2, 3])

p1 = Node[int](0)
q1 = Node[str]("Hello")

print(a1211.x)
print(d1211.x)
