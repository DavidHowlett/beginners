def double(x):
    return x * 2


def triple(x):
    return x * 3


def quadruple(x):
    return x * 4


def iainMap(x, y):
    """
    for j in y:
        for i in x:
            pass
    """
    return [[i(j) for i in x] for j in y]
