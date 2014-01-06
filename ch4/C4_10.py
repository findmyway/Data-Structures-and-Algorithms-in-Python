#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   calculate the integer part of the base-two logarithm of n
#
#   Create time: 2013-12-28 19:24:41


def log2_int(n):
    if n <= 0:
        raise ValueError('Input must greater than 0')
    elif 0 < n/2 < 1:
        return 0
    else:
        x = 1
        x += log2_int(n/2)
        return x

if __name__ == '__main__':
    for n in range(10):
        print('the integer part of the base-two logarithm of {0} is {1}'
              .format(2**n, log2_int(2**n)))
