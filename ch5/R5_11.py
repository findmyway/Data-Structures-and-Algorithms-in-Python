#!/usr/bin/env python3
#
#       Author:    TianJun
#       E-mail:    tianjun.cpp@gmail.com
#       Website:   www.tianjun.ml
#
#       File Name: R5_11.py
#       Description:
#           sum two dim data
#
#       Last Modified:
#           2014-06-26 19:12:21


from pprint import pprint
data = [[i for i in range(10)] for j in range(10)]
pprint(data)
sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        sum += data[i][j]
print("sum of data:", sum)
