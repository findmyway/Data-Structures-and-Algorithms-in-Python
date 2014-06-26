#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   reverse SequenceIterator
#
#   Create time: 2014-06-10 16:07:23

from sequence_iterator import SequenceIterator


class ReversedSequenceIterator(SequenceIterator):
    """An reversed iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        super().__init__(sequence)
        self._k = 0

    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1                  # advance to next index
        if -self._k <= len(self._seq):
            return(self._seq[self._k])  # return the data element
        else:
            raise StopIteration()       # there are no more elements

    def __str__(self):
        return "  ".join(str(next(self)) for i in self._seq)

if __name__ == '__main__':
    s = ReversedSequenceIterator([1, 2, 3])
    print(s)
