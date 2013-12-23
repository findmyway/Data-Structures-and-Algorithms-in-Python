import collections

class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:
      try:                                     # we test if param is iterable
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('invalid parameter type')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):          # relies on __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __sub__(self, b):
    """Return minus of two vectors"""
    if len(self) != len(b):
      raise ValueError('dimensions must agree')
    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = self[j] - b[j]
    return result

  def __neg__(self, ):
    """turn a vector into negtive"""
    result = Vector(len(self))
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other             # rely on existing __eq__ definition

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

  def __neg__(self):
    """Return copy of vector with all coordinates negated."""
    result = Vector(len(self))           # start with vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __lt__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords < other._coords

  def __le__(self, other):
    """Compare vectors based on lexicographical order."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    return self._coords <= other._coords

if __name__ == '__main__':
  # the following demonstrates usage of a few methods
  v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
  v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
  v[-1] = 45                 # <0, 23, 0, 0, 45> (also via __setitem__)
  print(v[4])                # print 45 (via __getitem__)
  u = v + v                  # <0, 46, 0, 0, 90> (via __add__)
  print(u)                   # print <0, 46, 0, 0, 90>
  u = -u
  print(u)
  u = v - v
  print(u)
  total = 0
  for entry in v:            # implicit iteration via __len__ and __getitem__
    total += entry
