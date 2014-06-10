#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: P1_36.py
#       Description:
#           count
#
#       Last Modified:
#           2014-06-10 14:16:16


def count(s):
    word_count = {}
    for word in s.split():
        word_count[word] = 1 + word_count.get(word, 0)
    print(word_count)

if __name__ == '__main__':
    s = input("input a sentance:\n")
    count(s)
