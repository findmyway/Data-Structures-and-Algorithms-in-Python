#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R6_4.py
#       Description:
#           recursively remove elements in stack
#
#       Last Modified:
#           2014-06-27 10:25:25


from array_stack import ArrayStack, Empty


def recursive_remove(s):
    if len(s) > 0:
        s.pop()
        recursive_remove(s)
    else:
        pass

if __name__ == '__main__':
    s = ArrayStack()
    for i in range(100):
        s.push(i)
    recursive_remove(s)
    try:
        s.pop()
    except Empty as e:
        print(e)
