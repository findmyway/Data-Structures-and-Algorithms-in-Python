#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C2_27.py
#       Description:
#           change the contain method of class Range
#
#       Last Modified:
#           2014-06-10 16:09:10

from range import Range
import timeit


class MyRange(Range):

    def __init__(self, start, stop=None, step=1):
        super().__init__(start, stop, step)

    def __contains__(self, val):
        r = (val - self._start) % self._step
        if r == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    t1 = timeit.Timer("99999 in Range(1, 100000, 2)",
                      "from range import Range")
    t2 = timeit.Timer("99999 in MyRange(1, 100000, 2)",
                      "from __main__ import MyRange")
    print("original Range Class, time consumes :", t1.timeit(100))
    print("MyRange Class, time consumes :", t2.timeit(100))
