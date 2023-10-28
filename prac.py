from typing import Iterator


def my_range1(start: int, end: int, step: int = 2) -> Iterator[int]:
    for i in range(start, end + 1, step):
        yield i
    return i


print(list(my_range1(1, 9, 1)))
