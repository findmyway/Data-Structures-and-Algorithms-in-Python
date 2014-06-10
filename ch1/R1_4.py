#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R1_4.py
#       Description:
#           sum square numbers less then given
#
#       Last Modified:
#           2014-06-10 11:18:08


def sum_square(k):
    assert k > 0
    return sum(x ** 2 for x in range(k))

if __name__ == '__main__':
    k = input("input num:")
    print("sum of square numbers less then {} is {}".
          format(k, sum_square(int(k))))
