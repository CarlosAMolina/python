# https://realpython.com/python-namedtuple/#using-namedtuple-to-write-pythonic-code

from typing import List, NamedTuple


class PlotValues(NamedTuple):
    x: List[int]
    y: List[int]


if __name__ == "__main__":
    values = PlotValues(
        x=[1,2,3],
        y=[4,5,6],
    )
    print("x", values.x)
    print("y", values.y)
    print("len", len(values)) # 2
