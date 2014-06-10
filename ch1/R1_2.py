#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R1_2.py
#       Description:
#           judge if an int is even
#
#       Last Modified:
#           2014-06-10 11:02:15


def is_even(k):
    return not k & 1

if __name__ == '__main__':
    k = input("input an int:")
    print("is even ?", is_even(int(k)))
