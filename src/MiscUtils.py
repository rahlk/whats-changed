from __future__ import division
import sys
import random
import math
from functools import reduce
sys.dont_write_bytecode = True


class Anon():
    "Anonymous container"
    def __init__(i, **fields):
        i.override(fields)

    def override(i, d):
        i.__dict__.update(d)
        return i

    def __repr__(i):
        d = i.__dict__
        name = i.__class__.__name__
        return name + '{' + ' '.join([':%s %s' % (k, pretty(d[k]))
                                      for k in i.show()]) + '}'

    def show(i):
        return [k for k in sorted(i.__dict__.keys())
                if not "_" in k]


def pairs(lst):
    "Return all pairs of items i,i+1 from a list."
    last = lst[0]
    for i in lst[1:]:
        yield last, i
        last = i
