#!/usr/bin/python
def dual(i):
    if isinstance(i, Dual):
        return i
    else:
        return Dual(float(i), 0.0)

class Dual(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(x, y):
        y = dual(y)
        return Dual(
            x.a + y.a,
            x.b + y.b
        )
    def __sub__(x, y):
        y = dual(y)
        return Dual(
            x.a - y.a,
            x.b - y.b
        )
    def __mul__(x, y):
        y = dual(y)
        return Dual(
            x.a * y.a,
            x.a*y.b + y.a*x.b
        )
    def __div__(x, y):
        y = dual(y)
        return Dual(
            x.a/y.a,
            (x.b*y.a - x.a*y.b) / (y.b*y.b)
        )

def deriv(f):
    def inner(a):
        return f( Dual(float(a), 1.0) ).b
    return inner

if __name__ == '__main__':
    from pylab import *
    def f(a):
        return a*a*a
    f1 = deriv(f) # 3*a*a

    x = arange(0.0, 4.0, 0.01)
    y1 = [f(i) for i in x]
    y2 = [f1(i) for i in x]
    plot(x, y1, 'g-', x, y2, 'g-', linewidth=1.0)
    show()
