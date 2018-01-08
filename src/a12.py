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
