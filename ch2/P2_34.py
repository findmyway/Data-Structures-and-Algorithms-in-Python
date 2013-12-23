#!/usr/bin/env python3
# Copyright 2013, Jun Tian
#
#   tianjun.cpp@gmail.com
#   www.tianjun.ml
#
#   DESCRIPTION:
#   plot the frequences of each alphabet
#
#   Create time: 2013-12-22 15:56:19


freqDic = {}
with open('P2_34.py') as f:
    #Read source file and calculate the frequences
    for line in f:
        for char in line:
            if char.isalpha():
                freqDic[char] = freqDic.get(char, 0) + 1
#plot the frequences
for alpha in range(ord('a'), ord('z')+1):
    alpha = chr(alpha)
    print("%s " % (alpha) + "-"*freqDic.get(alpha, 0))
for alpha in range(ord('A'), ord('Z')+1):
    alpha = chr(alpha)
    print("%s " % (alpha) + "-"*freqDic.get(alpha, 0))
