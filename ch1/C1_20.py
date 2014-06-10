#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_20.py
#       Description:
#           shuffle a list
#
#       Last Modified:
#           2014-06-10 12:31:43


def my_shuffle(data):
    """each time, generate two random indexes,
        then exchange them, repeat n times
        n is the length of data
    """
    from random import randint
    for i in range(len(data)):
        m = randint(0, len(data) - 1)
        n = randint(0, len(data) - 1)
        data[m], data[n] = data[n], data[m]

if __name__ == '__main__':
    a = [i for i in range(10)]
    print("initial list:", a)
    for i in range(10):
        my_shuffle(a)
        print("shuffled:", a)
