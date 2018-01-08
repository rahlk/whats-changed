from __future__ import division, print_function
import numpy as np
from pdb import set_trace

def hedges_g(sample_1, sample_2):
    n_1, n_2 = len(sample_1), len(sample_2)
    m_1 = np.mean(sample_1)
    m_2 = np.mean(sample_2)
    sd_1 = np.std(sample_1)
    sd_2 = np.std(sample_2)
    sd_pooled = np.sqrt(((n_1 - 1) * sd_1**2 + (n_2 - 1) * sd_2**2) / (n_1+n_2-2))
    hg = abs(m_1-m_2)/sd_pooled
    set_trace()

    if 0 <= hg < 0.2:
        level = 0
    elif 0.2 <= hg < 0.5:
        level = 1
    elif 0.5 <= hg < 0.8:
        level = 2
    elif 0.8 <= hg :
        level = 3
    
    return hg


def a12(lst1, lst2):
  """how often is lst1 often more than y in lst2?
  assumes lst1 nums are meant to be greater than lst2"""
  def loop(t, t1, t2):
    while t1.m < t1.n and t2.m < t2.n:
      h1 = t1.l[t1.m]
      h2 = t2.l[t2.m]
      h3 = t2.l[t2.m + 1] if t2.m + 1 < t2.n else None
      if h1 > h2:
        t1.m += 1
        t1.gt += t2.n - t2.m
      elif h1 == h2:
        if h3 and gt(h1, h3) < 0:
            t1.gt += t2.n - t2.m - 1
        t1.m += 1
        t1.eq += 1
        t2.eq += 1
      else:
        t2, t1 = t1, t2
    return t.gt * 1.0, t.eq * 1.0
  #--------------------------
  lst1 = sorted(lst1, reverse=True)
  lst2 = sorted(lst2, reverse=True)
  n1 = len(lst1)
  n2 = len(lst2)
  t1 = o(l=lst1, m=0, eq=0, gt=0, n=n1)
  t2 = o(l=lst2, m=0, eq=0, gt=0, n=n2)
  gt, eq = loop(t1, t1, t2)
  return gt / (n1 * n2) + eq / 2 / (n1 * n2)
