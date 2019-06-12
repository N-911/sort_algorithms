"""
dynamic programming algoritm
>>> clear()
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop(3)
3
"""

_stack = []

def push(x):
    _stack.append(x)
    """
    >>>size = len(_stack)
    >>>push(5)
    >>>len(_stack) - size
    1
    >>>stack[-1]
    5
    """


def pop():
    x = _stack.pop()
    return x


def clear():
    _stack.clear()


def is_empty():
    return len(_stack) == 0


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)