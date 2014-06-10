#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: C1_24.py
#       Description:
#           calculate number of vowels in a string
#
#       Last Modified:
#           2014-06-10 13:12:34


def n_vowels(s):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    n = 0
    for x in s:
        if x in vowels:
            n += 1
    return n
