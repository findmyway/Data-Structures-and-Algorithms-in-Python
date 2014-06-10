#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_27.py
#       Description:
#
#
#       Last Modified:
#           2014-06-10 13:53:29


def factors(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in reversed(temp):
        yield i
