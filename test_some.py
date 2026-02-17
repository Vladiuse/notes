from dataclasses import dataclass

print(1234)


@dataclass
class X:
    a: str | None


def func(num: int) -> int:
    """Docstring для xs."""
    return num


x = X(a=None)

func(num=x.a)

li = [1, 2, 3]

