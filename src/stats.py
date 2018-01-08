from __future__ import division, print_function

import numpy as np
import sys
from random import random as random
from random import choice as any
from random import seed
import math
from pdb import set_trace
from functools import reduce

from MathUtils import *
from MiscUtils import *


sys.dont_write_bytecode = True


def hedges_g(sample_1, sample_2):
    n_1, n_2 = len(sample_1), len(sample_2)
    m_1 = np.mean(sample_1)
    m_2 = np.mean(sample_2)
    sd_1 = np.std(sample_1)
    sd_2 = np.std(sample_2)
    sd_pooled = np.sqrt(((n_1 - 1) * sd_1**2 + (n_2 - 1)
                         * sd_2**2) / (n_1 + n_2 - 2))
    hg = abs(m_1 - m_2) / sd_pooled

    if 0 <= hg < 0.2:
        level = 0  # Very low
    elif 0.2 <= hg < 0.5:
        level = 1  # Medium low
    elif 0.5 <= hg < 0.8:
        level = 2  # Medium high
    elif 0.8 <= hg:
        level = 3  # Very high

    return hg


def a12(lst1, lst2):
    "how often is x in lst1 more than y in lst2?"
    def loop(t, t1, t2):
        while t1.j < t1.n and t2.j < t2.n:
            h1 = t1.l[t1.j]
            h2 = t2.l[t2.j]
            h3 = t2.l[t2.j + 1] if t2.j + 1 < t2.n else None
            if h1 > h2:
                t1.j += 1
                t1.gt += t2.n - t2.j
            elif h1 == h2:
                if h3 and h1 > h3:
                    t1.gt += t2.n - t2.j - 1
                t1.j += 1
                t1.eq += 1
                t2.eq += 1
            else:
                t2, t1 = t1, t2
        return t.gt * 1.0, t.eq * 1.0
    #--------------------------`
    lst1 = sorted(lst1, reverse=True)
    lst2 = sorted(lst2, reverse=True)
    n1 = len(lst1)
    n2 = len(lst2)
    t1 = Anon(l=lst1, j=0, eq=0, gt=0, n=n1)
    t2 = Anon(l=lst2, j=0, eq=0, gt=0, n=n2)
    gt, eq = loop(t1, t1, t2)
    return gt / (n1 * n2) + eq / 2 / (n1 * n2)
