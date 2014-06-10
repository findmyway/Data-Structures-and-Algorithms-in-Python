#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_26.py
#       Description:
#           varify  some expressions
#
#       Last Modified:
#           2014-06-10 13:28:47


if __name__ == '__main__':
    s = input("input three integers:(seperate by blank)").split()
    a, b, c = (int(i) for i in s)
    print("Is {} + {} = {} ?".format(a, b, c), a + b == c)
    print("Is {} = {} - {} ?".format(a, b, c), a == b - c)
    print("Is {} = {} * {} ?".format(a, b, c), a == b * c)
