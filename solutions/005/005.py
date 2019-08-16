def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(f):
    return f(lambda x, y: x)


def cdr(f):
    return f(lambda x, y: y)


assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4
