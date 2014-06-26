#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R5_14.py
#       Description:
#           my shuffle
#
#       Last Modified:
#           2014-06-26 19:23:54
from random import randrange


def my_shuffle(d):
    a = []
    for k in range(len(d)):
        i = randrange(len(d))
        a.append(d.pop(i))
    return a


if __name__ == '__main__':
    d = [i for i in range(10)]
    print("origin data:", d)
    a = my_shuffle(d)
    print("shuffled data:", a)
