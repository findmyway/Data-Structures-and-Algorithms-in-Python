#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R1_7.py
#       Description:
#            the sum of the squares of all the odd positive integers smaller
#            than n.
#
#       Last Modified:
#           2014-06-10 11:24:51


def sum_square(k):
    assert k > 0
    return sum(x ** 2 for x in range(k) if x & 1)

if __name__ == '__main__':
    k = input("input num:")
    print("sum of squares of odd numbers less then {} is {}".
          format(k, sum_square(int(k))))
