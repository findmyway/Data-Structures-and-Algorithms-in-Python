#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: P1_30.py
#       Description:
#
#
#       Last Modified:
#           2014-06-10 14:02:24
from math import floor, log2


if __name__ == '__main__':
    n = int(input("input an integer:"))
    assert n > 2
    print("Need {} times to divide".format(int(floor(log2(n)))))
