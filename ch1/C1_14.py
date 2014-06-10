#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_14.py
#       Description:
#           calculate determines if there is a distinct pair of numbers in the
#           sequence whose product is odd.
#
#       Last Modified:
#           2014-06-10 11:42:15


def is_product_odd_in(s):
    """just count the num of odd in a sequence"""
    result = False
    for d in s:
        if d % 2 == 1:
            result = True
            break
    return result

if __name__ == '__main__':
    s = input("input integers, seperate by blank(at least 2 numbers):")
    s = [int(a) for a in s.split()]
    print("is there a pair of numbers whose product is odd?\n",
          is_product_odd_in(s))
