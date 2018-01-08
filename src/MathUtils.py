from __future__ import division
import sys
import random
import math
from functools import reduce
sys.dont_write_bytecode = True


def exp(n): return math.e ** n


def ln(n): return math.log(n, math.e)


def g(n): return round(n, 2)


def median(lst, ordered=False):
    if not ordered:
        lst = sorted(lst)
    n = len(lst)
    p = n // 2
    if n % 2:
        return lst[p]
    q = p - 1
    q = max(0, min(q, n))
    return (lst[p] + lst[q]) / 2


def msecs(f):
    import time
    t1 = time.time()
    f()
    return (time.time() - t1) * 1000


class Num:

    "An Accumulator for numbers"
    def __init__(i, name, inits=[]):
        i.n = i.m2 = i.mu = 0.0
        i.all = []
        i._median = None
        i.name = name
        i.rank = 0
        for x in inits:
            i.add(x)

    def s(i):
        return (i.m2 / (i.n - 1)) ** 0.5

    def add(i, x):
        i._median = None
        i.n += 1
        i.all += [x]
        delta = x - i.mu
        i.mu += delta * 1.0 / i.n
        i.m2 += delta * (x - i.mu)

    def __add__(i, j):
        return Num(i.name + j.name, i.all + j.all)

    def quartiles(i):
        def p(x):
            return int(100 * g(xs[x]))
        i.median()
        xs = i.all
        n = int(len(xs) * 0.25)
        return p(n), p(2 * n), p(3 * n)

    def median(i):
        if not i._median:
            i.all = sorted(i.all)
            i._median = median(i.all)
        return i._median

    def __lt__(i, j):
        return i.median() < j.median()

    def spread(i):
        i.all = sorted(i.all)
        n1 = i.n * 0.25
        n2 = i.n * 0.75
        if len(i.all) <= 1:
            return 0
        if len(i.all) == 2:
            return i.all[1] - i.all[0]
        else:
            return i.all[int(n2)] - i.all[int(n1)]
