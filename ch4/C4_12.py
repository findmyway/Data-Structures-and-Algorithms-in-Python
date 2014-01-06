#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   algorithm to compute the product of two positive integers,
#   m and n, using only addition and subtraction.
#
#   Create time: 2013-12-28 19:40:48


def product(m, n):
    sign = (n >= 0)
    n = abs(n)
    if n > 0:
        result = m + product(m, n-1)
    else:
        result = 0
    return result if sign else -result

if __name__ == '__main__':
    for x in range(5):
        print('the product of {0} and {1} is {2}'
              .format(x, x+1, product(x, x+1)))
        print('the product of {0} and {1} is {2}'
              .format(-x, x+1, product(-x, x+1)))
