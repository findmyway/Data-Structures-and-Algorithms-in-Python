#!/usr/bin/env python

from progressions import FibonacciProgression
f = FibonacciProgression(2, 2)
for i in range(8 - 1):
    f._advance()
f.print_progression(1)
