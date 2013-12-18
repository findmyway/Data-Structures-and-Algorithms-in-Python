#!/usr/bin/env python3
# Author: TianJun
# Mail: find_my_way@foxmail.com
# Created Time: 2013/12/16 19:46:32
def pNorm(v, p):
    sum = 0
    for x in v:
        sum += x ** p
    norm = sum ** (1/p)
    return norm
if __name__ == '__main__':
    test = pNorm([4, 3], 2)
    print(test)
