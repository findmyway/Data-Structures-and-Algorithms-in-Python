#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R6_5.py
#       Description:
#           reverse list use stack
#
#       Last Modified:
#           2014-06-27 10:33:45


from array_stack import ArrayStack, Empty


def reverse(L):
    s = ArrayStack()
    for i in range(len(L)):
        s.push(L[i])
    for i in range(len(L)):
        L[i] = s.pop()

if __name__ == '__main__':
    L = [i for i in range(10)]
    print(L)
    reverse(L)
    print('reversed L:\n', L)
