#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_22.py
#       Description:
#           dot prodction
#
#       Last Modified:
#           2014-06-10 13:05:36


def dot_product(a, b):
    assert len(a) == len(b)
    return [a[i] * b[i] for i in range(len(a))]

if __name__ == '__main__':
    a = [i for i in range(5)]
    b = [i for i in range(5)]
    print("a = ", a)
    print("b = ", b)
    print("a dot b = ", dot_product(a, b))
