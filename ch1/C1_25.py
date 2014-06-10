#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_25.py
#       Description:
#           remove punctuation in a string
#
#       Last Modified:
#           2014-06-10 13:19:26


def remove_punctuation(s):
    return ''.join(x for x in s if x.isalnum() or x.isspace())

if __name__ == '__main__':
    s = input("input a string\n")
    print("removed string is:")
    print(remove_punctuation(s))
