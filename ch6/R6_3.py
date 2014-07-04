#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R6_3.py
#       Description:
#           transfer stack
#
#       Last Modified:
#           2014-06-27 10:15:20


from array_stack import ArrayStack, Empty


def transfer(s, t):
    while(len(s)>0):
        t.push(s.pop())

if __name__ == '__main__':
    s = ArrayStack()
    t = ArrayStack()
    for i in range(10):
        s.push(i)
    transfer(s, t)
    for i in range(10):
        print(t.pop())
