#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   find max min value using recursion
#
#   Create time: 2013-12-23 10:54:50


def find_MaxMin(data, l, r):
    mid = (l + r) // 2
    if l == mid:
        return min(data[l], data[r]), max(data[l], data[r])
    else:
        lmin, lmax = find_MaxMin(data, l, mid)
        rmin, rmax = find_MaxMin(data, mid, r)
        return min(lmin, rmin), max(lmax, rmax)

if __name__ == '__main__':
    a, b = find_MaxMin([3, 8, 10, 0, 7], 0, 4)
    print("min is {0} \
          max is {1}".format(a, b))
